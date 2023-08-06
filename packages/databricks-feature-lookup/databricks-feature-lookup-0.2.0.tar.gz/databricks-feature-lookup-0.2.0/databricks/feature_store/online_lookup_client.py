from databricks.feature_store.entities.online_feature_table import (
    AbstractOnlineFeatureTable,
    OnlineFeatureTable,
    OnlineFeatureTableForSageMakerServing,
)
from databricks.feature_store.entities.store_type import StoreType
from databricks.feature_store.lookup_engine import (
    AwsAccessKey,
    LookupMySqlEngine,
    LookupSqlEngine,
    LookupSqlServerEngine,
    LookupEngine,
    LookupDynamoDbEngine,
    LookupCosmosDbEngine,
)
from databricks.feature_store.mlflow_model_constants import DATABRICKS, SAGEMAKER

from typing import List, Tuple, Optional
import pandas as pd
import os

# The provisioner of this model is expected to set the following environment variable for each
# feature table if the feature store is SQL based:
#  (1) <online_store_for_serving.read_secret_prefix>_USER
#  (2) <online_store_for_serving.read_secret_prefix>_PASSWORD
USER_SUFFIX = "_USER"
PASSWORD_SUFFIX = "_PASSWORD"
# For DynamoDB the following variables should be set:
#  (1) <online_store_for_serving.read_secret_prefix>_ACCESS_KEY_ID
#  (2) <online_store_for_serving.read_secret_prefix>_SECRET_ACCESS_KEY
ACCESS_KEY_ID_SUFFIX = "_ACCESS_KEY_ID"
SECRET_ACCESS_KEY_SUFFIX = "_SECRET_ACCESS_KEY"
# For Cosmos DB the following variable should be set:
#  (1) <online_store_for_serving.read_secret_prefix>_AUTHORIZATION_KEY
AUTHORIZATION_KEY_SUFFIX = "_AUTHORIZATION_KEY"


def generate_lookup_sql_engine(
    online_feature_table: OnlineFeatureTable,
    creds: Tuple[str, str],
) -> LookupSqlEngine:
    ro_user, ro_password = creds
    if online_feature_table.online_store.store_type == StoreType.SQL_SERVER:
        return LookupSqlServerEngine(online_feature_table, ro_user, ro_password)
    return LookupMySqlEngine(online_feature_table, ro_user, ro_password)


def generate_lookup_dynamodb_engine(
    online_feature_table: AbstractOnlineFeatureTable,
    creds: Optional[Tuple[str, str]],
) -> LookupDynamoDbEngine:
    if creds:
        access_key_id, secret_access_key = creds

        return LookupDynamoDbEngine(
            online_feature_table,
            access_key=AwsAccessKey(access_key_id, secret_access_key),
        )
    else:
        return LookupDynamoDbEngine(online_feature_table, access_key=None)


def generate_lookup_cosmosdb_engine(
    online_feature_table: OnlineFeatureTable, creds: str
) -> LookupCosmosDbEngine:
    return LookupCosmosDbEngine(online_feature_table, authorization_key=creds)


def load_credentials_from_env(online_ft: OnlineFeatureTable):
    def get_env_var(env_var_suffix: str) -> str:
        env_var = online_ft.online_store.read_secret_prefix + env_var_suffix
        if env_var not in os.environ:
            raise Exception(
                f"Internal error: {env_var} not found for feature table {online_ft.feature_table_name}."
            )
        return os.getenv(env_var)

    if online_ft.online_store.store_type == StoreType.DYNAMODB:
        return (
            get_env_var(ACCESS_KEY_ID_SUFFIX),
            get_env_var(SECRET_ACCESS_KEY_SUFFIX),
        )
    elif online_ft.online_store.store_type == StoreType.COSMOSDB:
        return get_env_var(AUTHORIZATION_KEY_SUFFIX)
    else:
        return (
            get_env_var(USER_SUFFIX),
            get_env_var(PASSWORD_SUFFIX),
        )


class OnlineLookupClient:
    def __init__(
        self, online_feature_table: AbstractOnlineFeatureTable, serving_environment: str
    ):
        self.lookup_engine = self._generate_lookup_engine(
            online_feature_table, serving_environment
        )

    @staticmethod
    def _generate_lookup_engine(
        online_feature_table: AbstractOnlineFeatureTable, serving_environment: str
    ):
        if serving_environment == DATABRICKS:
            if not isinstance(online_feature_table, OnlineFeatureTable):
                raise Exception(
                    "Internal Error: Expected OnlineFeatureTable when serving_environment=DATABRICKS"
                    f". Got {type(online_feature_table)}."
                )
            return OnlineLookupClient._generate_lookup_engine_databricks(
                online_feature_table
            )

        elif serving_environment == SAGEMAKER:
            if not isinstance(
                online_feature_table, OnlineFeatureTableForSageMakerServing
            ):
                raise Exception(
                    "Internal Error: Expected OnlineFeatureTableForSageMakerServing when "
                    f"serving_environment=DATABRICKS. Got {type(online_feature_table)}."
                )
            return OnlineLookupClient._generate_lookup_engine_sagemaker(
                online_feature_table
            )

        raise Exception(
            f"Internal Error: Unexpected serving_environment {serving_environment}."
        )

    @classmethod
    def _generate_lookup_engine_databricks(
        cls, online_feature_table: OnlineFeatureTable
    ):
        creds = load_credentials_from_env(online_feature_table)
        if online_feature_table.online_store.store_type == StoreType.DYNAMODB:
            return generate_lookup_dynamodb_engine(online_feature_table, creds)
        elif online_feature_table.online_store.store_type == StoreType.COSMOSDB:
            return generate_lookup_cosmosdb_engine(online_feature_table, creds)
        else:
            return generate_lookup_sql_engine(online_feature_table, creds)

    @classmethod
    def _generate_lookup_engine_sagemaker(
        cls, online_feature_table: OnlineFeatureTableForSageMakerServing
    ):
        return generate_lookup_dynamodb_engine(online_feature_table, creds=None)

    def lookup_features(
        self,
        lookup_df: pd.DataFrame,
        feature_names: List[str],
    ) -> pd.DataFrame:
        """Uses a Python database connection to lookup features in feature_names using
        the lookup keys and values in lookup_df. The online store database and table name are
        obtained from the AbstractOnlineFeatureTable passed to the constructor.

        The resulting DataFrame has the same number of rows as lookup_df. In the case that a lookup
        key cannot be found, a row of NaNs will be returned in the resulting DataFrame.

        Throws an exception if the table, lookup keys, or feature columns do not exist in the
        online store.

        :param lookup_df: Pandas DataFrame containing lookup keys and values. The DataFrame should
        contain one column for each primary key of the online feature table, and one row for each
        entity to look up.
        :param feature_names: A list of feature names to look up.
        :return: Pandas DataFrame containing feature keys and values fetched from the online store.
        """
        features = self.lookup_engine.lookup_features(
            lookup_df,
            feature_names,
        )
        return features

    def cleanup(self):
        """
        Performs any cleanup associated with the online store.
        :return:
        """
        self.lookup_engine.shutdown()
