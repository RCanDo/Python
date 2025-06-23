import subprocess
from datetime import datetime
import datetime as dt

import pandas as pd

from utils import df as udf
from utils.config import pandas_options
pandas_options()

from feast import FeatureStore
from feast.data_source import PushMode

import os
os.chdir('ak1/feature_repo/')

# %%
df = pd.read_parquet("data/driver_stats.parquet")
udf.info(df)
udf.summary(df)

df[df.driver_id==1001].sort_values(["event_timestamp"]).iloc[:5,]
df[df.driver_id==1001].sort_values(["event_timestamp"]).iloc[-5:,]

df[df.driver_id==1002].sort_values(["event_timestamp"]).iloc[:5,]
df[df.driver_id==1002].sort_values(["event_timestamp"]).iloc[-5:,]

df[df.driver_id==1003].sort_values(["event_timestamp"]).iloc[:5,]
df[df.driver_id==1003].sort_values(["event_timestamp"]).iloc[-5:,]

DATE_0 = min(df.event_timestamp)
DATE_1 = max(df.event_timestamp)

DATE_0
DATE_1

# %% create fake new records to offline store
idx_max = df.index.max()
df.driver_id.unique()   # array([1005, 1004, 1003, 1002, 1001])

df_new = pd.DataFrame(columns=df.columns)
for driver_id in df.driver_id.unique():
    df_k = df[df.driver_id==driver_id].sort_values(["event_timestamp"]).iloc[:-30,].sample(5)
    df_k.event_timestamp = [DATE_1 + dt.timedelta(hours=k + 1) for k in range(5)]
    df_new = pd.concat([df_new, df_k])

df_new.index = list(range(idx_max + 1, idx_max + len(df_new) + 1))
df_all = pd.concat([df, df_new])
df_all.to_parquet("data/driver_stats_1.parquet")

# %%
store = FeatureStore(repo_path=".")
print("\n--- Run feast apply ---")
subprocess.run(["feast", "apply"])

# %%
FEATURES = [
    "driver_hourly_stats:conv_rate",
    "driver_hourly_stats:acc_rate",
    "driver_hourly_stats:avg_daily_trips",
    "transformed_conv_rate:conv_rate_plus_val1",
    "transformed_conv_rate:conv_rate_plus_val2",
]

entity_df = pd.DataFrame.from_dict(
    {
        # entity's join key -> entity values
        "driver_id": [1001, 1002, 1003],
        # "event_timestamp" (reserved key) -> timestamps
        "event_timestamp": [
            datetime(2021, 4, 12, 10, 59, 42),
            datetime(2021, 4, 12, 8, 12, 10),
            datetime(2021, 4, 12, 16, 40, 26),
        ],
        # (optional) label name -> label values. Feast does not process these
        "label_driver_reported_satisfaction": [1, 5, 3],   # just as example – no use of it here
        # values we're using for an on-demand transformation
        "val_to_add": [1, 2, 3],
        "val_to_add_2": [10, 20, 30],
    }
)
entity_df

hf = store.get_historical_features(
    entity_df=entity_df,             # ~ `inputs`  in  `transformed_conv_rate`
    features=FEATURES,
).to_df()
hf

# %%
entity_df_0 = entity_df.copy()
entity_df_0["event_timestamp"] = DATE_0

hf0 = store.get_historical_features(
    entity_df=entity_df_0,
    features=FEATURES,
).to_df()
hf0

# %% for_batch_scoring:
entity_df_1 = entity_df.copy()
DATE_CURRENT = DATE_1 + dt.timedelta(hours=24)   # !
entity_df_1["event_timestamp"] = DATE_CURRENT

hf1 = store.get_historical_features(
    entity_df=entity_df_1,
    features=FEATURES,
).to_df()
hf1

# %%
c_driver = df.driver_id.isin((1001, 1002, 1003))    # c_  like 'condition'

c_date = df.event_timestamp.dt.date == dt.date(2021, 4, 12)
df[c_driver & c_date].sort_values(['driver_id'])
hf0

c_date_1 = df.event_timestamp == DATE_1
df[c_driver & c_date_1].sort_values(['driver_id'])
hf1

# %%
print("\n--- Load features into online store ---")
# store.materialize_incremental(end_date=datetime.now())
store.materialize_incremental(end_date=dt.datetime.fromtimestamp(DATE_1.timestamp()) - dt.timedelta(hours=3))

# %%  fetch_online_features(store, source=...)
# print("\n--- Online features ---")
# source=""
# print("\n--- Online features retrieved (instead) through a feature service ---")
# source="feature_service_v1"
# source="feature_service_v2"
# print("\n--- Online features retrieved (using feature service v3, which uses a feature view with a push source ---")
source="push"

# # fetch_online_features(store, source)

entity_rows = [
    # {join_key: entity_value}
    {
        "driver_id": 1001,
        "val_to_add": 1000,
        "val_to_add_2": 2000,
    },
    {
        "driver_id": 1002,
        "val_to_add": 1001,
        "val_to_add_2": 2002,
    },
]

if source == "feature_service_v1":
    features_to_fetch = store.get_feature_service("driver_activity_v1")
elif source == "feature_service_v2":
    features_to_fetch = store.get_feature_service("driver_activity_v2")
elif source == "push":
    features_to_fetch = store.get_feature_service("driver_activity_v3")
else:
    features_to_fetch = [
        "driver_hourly_stats:acc_rate",
        "transformed_conv_rate:conv_rate_plus_val1",
        "transformed_conv_rate:conv_rate_plus_val2",
    ]

returned_features = store.get_online_features(
    features=features_to_fetch,
    entity_rows=entity_rows,
).to_df()

returned_features

# %%
print("\n--- Simulate a stream event ingestion of the hourly stats df ---")
event_new = pd.DataFrame.from_dict(
    {
        "__index_level_0__": [1833],
        "driver_id": [1002],
        "event_timestamp": [pd.Timestamp.utcnow()],  # better use pd.Timestamp
        "created": [datetime.now()],
        "conv_rate": [0.99],
        "acc_rate": [0.88],
        "avg_daily_trips": [777],
    }
)
event_new

store.push("driver_stats_push_source", event_new, to=PushMode.ONLINE_AND_OFFLINE)

# %%
print("\n--- Online features again with updated values from a stream push ---")
fetch_online_features(store, source="push")

# %%
print("\n--- Run feast teardown ---")
subprocess.run(["feast", "teardown"])


