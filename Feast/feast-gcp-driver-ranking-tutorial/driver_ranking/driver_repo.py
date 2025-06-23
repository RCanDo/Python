from datetime import timedelta

from feast import BigQuerySource, Entity, Field, FeatureView, ValueType
from feast.types import Float32, Float64, Int64

driver = Entity(
    name="driver_id",
    join_keys=["driver_id"],    # join_key="driver_id",
    value_type=ValueType.INT64,
)

driver_stats_source = BigQuerySource(
    table="feast-oss.demo_data.driver_hourly_stats",    # table_ref=
    timestamp_field="datetime",                         # event_timestamp_column=
    created_timestamp_column="created",
)

driver_stats_fv = FeatureView(
    name="driver_hourly_stats",
    entities=[driver],     # =["driver_id"],
    ttl=timedelta(weeks=52),
    schema=[
        Field(name="conv_rate", dtype=Float32),
        Field(name="acc_rate", dtype=Float32),
        Field(name="avg_daily_trips", dtype=Int64, description="Average daily trips"),
    ],
    # features=[
    #     Feature(name="conv_rate", dtype=ValueType.FLOAT),
    #     Feature(name="acc_rate", dtype=ValueType.FLOAT),
    #     Feature(name="avg_daily_trips", dtype=ValueType.INT64),
    # ],
    source=driver_stats_source,             # input=
    tags={"team": "driver_performance"},
)
