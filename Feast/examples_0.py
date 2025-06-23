"""
https://docs.feast.dev/getting-started/concepts/feature-retrieval
"""

# %%
import pandas as pd
import datetime as dt

from utils.config import pandas_options
pandas_options()

from utils import df as udf

# %%
df = pd.read_parquet("data/driver_stats.parquet")
udf.info(df)


max(df.event_timestamp)                         # Timestamp('2024-10-07 08:00:00+0000', tz='UTC')
max(df[df.driver_id==1001].event_timestamp)     # 0.94787055
max(df[df.driver_id==1002].event_timestamp)     # 0.49857682

df[df.driver_id==1001].sort_values(['event_timestamp']).conv_rate.iloc[-1]
df[df.driver_id==1002].sort_values(['event_timestamp']).conv_rate.iloc[-1]

df[df.driver_id==1001].sort_values(['event_timestamp']).acc_rate.iloc[-1]
df[df.driver_id==1002].sort_values(['event_timestamp']).acc_rate.iloc[-1]

# %%
df[df.driver_id==1001].event_timestamp.sort_values().iloc[-22:]

c_driver = df.driver_id.isin((1001, 1002, 1003))
c_date = df.event_timestamp.dt.date == dt.date(2021, 4, 12)

df[c_driver & c_date].sort_values(['driver_id'])
hf0
hf1

df.loc[1803].event_timestamp    # Timestamp('2024-10-07 08:00:00+0000', tz='UTC')
dt.datetime(2024, 10, 7, 8)     # datetime.datetime(2024, 10, 7, 8, 0)
df.loc[1803].event_timestamp == dt.datetime(2024, 10, 7, 8, 0)  # False
df.loc[1803].event_timestamp == pd.to_datetime(dt.datetime(2024, 10, 7, 8))     # False
df.loc[1803].event_timestamp == pd.to_datetime(dt.datetime(2024, 10, 7, 8), utc=True)   # ok

c_date_2 = df.event_timestamp == pd.to_datetime(dt.datetime(2024, 10, 7, 8), utc=True)
df[c_driver & c_date_2].sort_values(['driver_id'])
hf10
hf11

# %%
df1 = pd.read_parquet("../../ak1/feature_repo/data/driver_stats.parquet")

# %% go to test_workflow.py first
from feast import FeatureStore

store = FeatureStore(repo_path=".")
dir(store)

store.list_all_feature_views()
store.list_batch_feature_views()
store.list_data_sources()
store.list_entities()
store.list_feature_services()
store.list_feature_views()
store.list_on_demand_feature_views()
store.list_stream_feature_views()

# %%
from feast import FeatureStore

feature_store = FeatureStore('.')  # Initialize the feature store

entity_df = pd.DataFrame.from_dict(
    {
        "driver_id": [1001, 1002, 1003, 1004, 1001],
        "event_timestamp": [
            datetime(2021, 4, 12, 10, 59, 42),
            datetime(2021, 4, 12, 8, 12, 10),
            datetime(2021, 4, 12, 16, 40, 26),
            datetime(2021, 4, 12, 15, 1, 12),
            datetime.now()
        ]
    }
)

training_df = store.get_historical_features(
    entity_df=entity_df,
    features=store.get_feature_service("model_v1"),
).to_df()

print(training_df.head())


# %%
from feast import FeatureStore

store = FeatureStore(repo_path=".")

# Get the latest feature values for unique entities
entity_sql = f"""
    SELECT
        driver_id,
        CURRENT_TIMESTAMP() as event_timestamp
    FROM {store.get_data_source("driver_hourly_stats_source").get_table_query_string()}
    WHERE event_timestamp BETWEEN '2021-01-01' and '2021-12-31'
    GROUP BY driver_id
"""
batch_scoring_features = store.get_historical_features(
    entity_df=entity_sql,
    features=store.get_feature_service("model_v2"),
).to_df()
# predictions = model.predict(batch_scoring_features)


# %%
from feast import FeatureStore, RepoConfig
from datetime import datetime, timedelta
fs = FeatureStore(
    repo_path=”project/feature_repo”
)
fs.materialize(
    start_date=datetime.utcnow() - timedelta(hours=3),
    end_date=datetime.utcnow() - timedelta(minutes=10)
)
# Materializing… <BLANKLINE> …
# %%