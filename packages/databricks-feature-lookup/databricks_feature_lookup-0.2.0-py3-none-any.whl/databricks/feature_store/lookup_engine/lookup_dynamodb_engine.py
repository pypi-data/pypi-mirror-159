""" Defines the LookupDynamoDbEngine class, which is used to perform lookups on DynamoDB store.
"""

import functools
import logging
from typing import List, Dict, Any, Optional

import numpy as np
import pandas as pd
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

from databricks.feature_store.entities.online_feature_table import (
    AbstractOnlineFeatureTable,
)
from databricks.feature_store.entities.query_mode import QueryMode
from databricks.feature_store.lookup_engine.lookup_engine import LookupEngine
from databricks.feature_store.utils.dynamodb_utils import (
    get_dynamodb_resource,
    key_schemas_equal,
    to_dynamodb_primary_key,
    to_range_schema,
    to_safe_select_expression,
    TABLE,
    KEY_SCHEMA,
    ITEM,
    ITEMS,
    PRIMARY_KEY_SCHEMA,
    PRIMARY_KEY_ATTRIBUTE_NAME_VALUE,
)
from databricks.feature_store.utils.dynamodb_type_utils import (
    DYNAMODB_DATA_TYPE_CONVERTER_FACTORY,
)

_logger = logging.getLogger(__name__)


class AwsAccessKey:
    def __init__(self, access_key_id: str, secret_access_key: str):
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key


class LookupDynamoDbEngine(LookupEngine):
    def __init__(
        self,
        online_feature_table: AbstractOnlineFeatureTable,
        access_key: Optional[AwsAccessKey],
    ):
        """
        :param online_feature_table: AbstractOnlineFeatureTable to look up feature values from.
        :param access_key: Uses this access key to authenticate with AWS, if provided. If None,
        role-based authentication is used. For example, SageMaker lookup passes access_key=None, and
        the SageMaker execution role is used to authenticate.
        """
        self.query_mode = online_feature_table.online_store.query_mode
        self.timestamp_keys = online_feature_table.timestamp_keys

        self.table_name = online_feature_table.online_feature_table_name
        self.region = online_feature_table.online_store.extra_configs.region

        self.primary_keys_to_type_converter = {
            pk.name: DYNAMODB_DATA_TYPE_CONVERTER_FACTORY.get_converter(pk)
            for pk in online_feature_table.primary_keys
        }
        self.features_to_type_converter = {
            feature.name: DYNAMODB_DATA_TYPE_CONVERTER_FACTORY.get_converter(feature)
            for feature in online_feature_table.features
        }

        self._dynamodb_resource = get_dynamodb_resource(
            access_key_id=access_key.access_key_id if access_key else None,
            secret_access_key=access_key.secret_access_key if access_key else None,
            region=self.region,
        )
        self._dynamodb_client = self._dynamodb_resource.meta.client
        self._validate_online_feature_table()

        self._dynamodb_table = self._dynamodb_resource.Table(self.table_name)

    def lookup_features(
        self, lookup_df: pd.DataFrame, feature_names: List[str]
    ) -> pd.DataFrame:
        query = functools.partial(self._run_lookup_dynamodb_query, feature_names)
        feature_df = lookup_df.apply(query, axis=1, result_type="expand")
        feature_df.columns = feature_names
        return feature_df

    def _validate_online_feature_table(
        self,
    ) -> None:
        # Fetch the online feature table from online store as specified by the OnlineFeatureTable if
        # exists else throw an error.
        try:
            table_desc = self._dynamodb_client.describe_table(TableName=self.table_name)
            # All table descriptions contain the key schema
            key_schema = table_desc[TABLE][KEY_SCHEMA]
        except ClientError as ce:
            raise ce

        def _validate_schema_for_pk_lookup():
            """
            Checks KeySchema equals: [{"AttributeName": "_feature_store_internal__primary_keys", "KeyType": "HASH"}]
            """
            if not key_schemas_equal(key_schema, [PRIMARY_KEY_SCHEMA]):
                raise ValueError(
                    f"Online Table {self.table_name} primary key schema is not configured properly."
                )

        def _validate_schema_for_range_lookup():
            """
            Checks KeySchema equals, in any order:
            [
                {"AttributeName": "_feature_store_internal__primary_keys", "KeyType": "HASH"},
                {"AttributeName": <timestamp key>, "KeyType": "RANGE"},
            ]
            """
            range_schema = to_range_schema(self.timestamp_keys[0].name)
            if not key_schemas_equal(key_schema, [PRIMARY_KEY_SCHEMA, range_schema]):
                raise ValueError(
                    f"Online Table {self.table_name} composite key schema is not configured properly."
                )

        if self.query_mode == QueryMode.PRIMARY_KEY_LOOKUP:
            _validate_schema_for_pk_lookup()
        elif self.query_mode == QueryMode.RANGE_QUERY:
            _validate_schema_for_range_lookup()
        else:
            raise ValueError(f"Unsupported query mode: {self.query_mode}")

    def _lookup_primary_key(
        self, dynamodb_primary_key: Dict[str, str], feature_names: List[str]
    ):
        response = self._dynamodb_table.get_item(
            Key=dynamodb_primary_key,
            AttributesToGet=feature_names,
        )
        # Response is expected to have form {"Item": {...}, ...}
        return response.get(ITEM, None)

    def _lookup_range_query(
        self, dynamodb_primary_key: Dict[str, str], feature_names: List[str]
    ):
        response = self._dynamodb_table.query(
            ScanIndexForward=False,
            Limit=1,
            KeyConditionExpression=Key(PRIMARY_KEY_ATTRIBUTE_NAME_VALUE).eq(
                dynamodb_primary_key[PRIMARY_KEY_ATTRIBUTE_NAME_VALUE]
            ),
            **to_safe_select_expression(feature_names),
        )
        # Response is expected to have form {"Items": [{...}], ...}
        items = response.get(ITEMS, [])
        return items[0] if len(items) else None

    def _run_lookup_dynamodb_query(
        self, feature_names: List[str], lookup_row: pd.core.series.Series
    ):
        """
        This helper function executes a single DynamoDB query.
        """
        dynamodb_lookup_row = self._pandas_to_dynamodb(lookup_row)
        dynamodb_primary_key = to_dynamodb_primary_key(dynamodb_lookup_row)
        if self.query_mode == QueryMode.PRIMARY_KEY_LOOKUP:
            feature_values = self._lookup_primary_key(
                dynamodb_primary_key, feature_names
            )
        elif self.query_mode == QueryMode.RANGE_QUERY:
            feature_values = self._lookup_range_query(
                dynamodb_primary_key, feature_names
            )
        else:
            raise ValueError(f"Unsupported query mode: {self.query_mode}")

        if not feature_values:
            _logger.warning(
                f"No feature values found in {self.table_name} for {dynamodb_lookup_row}."
            )
            return np.full(len(feature_names), np.nan)

        # Return the result
        results = [feature_values.get(f, np.nan) for f in feature_names]
        return self._dynamodb_to_pandas(results, feature_names)

    def _pandas_to_dynamodb(self, row: pd.core.series.Series) -> List[Any]:
        """
        Converts the input Pandas row to dynamodb compatible python types based on
        the input.
        :return:list[string, ...]
        """
        return [
            self.primary_keys_to_type_converter[pk_name].to_online_store(pk_value)
            for pk_name, pk_value in row.items()
        ]

    def _dynamodb_to_pandas(
        self, results: List[Any], feature_names: List[str]
    ) -> List[Any]:
        """
        Converts the input results list with dynamodb-compatible python values to pandas types based on
        the input features_names and features converter.
        :return:List[Any]
        """
        feature_names_and_values = zip(feature_names, results)
        return [
            self.features_to_type_converter[feature_name].to_pandas(feature_value)
            for feature_name, feature_value in feature_names_and_values
        ]

    def shutdown(self) -> None:
        """
        Cleans up the store connection if it exists on the DynamoDB online store.
        :return:
        """
        # DynamoDB connections are stateless http connections and hence do not need an explicit
        # shutdown operation.
        pass
