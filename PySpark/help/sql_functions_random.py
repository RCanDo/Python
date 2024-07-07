#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
title: generating random numbers
content:
    - rand()
    - randn()
    - cum_dist()
sources:
    - https://stackoverflow.com/questions/50366604/pyspark-create-dataframe-from-random-uniform-disribution
file:
    date: 2024-06-07
"""


# %%
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('sql_functions_01').getOrCreate()

from pyspark.sql import functions as f, DataFrame, types, Window


# %%
spark.range(2).withColumn('randn', f.randn(seed=42)).show()
# +---+--------------------+
# | id|               randn|
# +---+--------------------+
# |  0|  0.8951356612564867|
# |  1|-0.06706288020621906|
# +---+--------------------+

spark.range(2).withColumn('rand', f.rand(seed=42)).show()
# +---+------------------+
# | id|              rand|
# +---+------------------+
# |  0|0.6712601471691363|
# |  1|0.9676898928895498|
# +---+------------------+


# %%
def generate_random_normal_df(nrows, ncols, seed=1):
    df = spark.range(nrows)
    df = df.select('*', *(f.randn(seed).alias(f"c{c}") for c in range(ncols)))
    return df.drop("id")

df = generate_random_normal_df(nrows=4, ncols=3, seed=1)
df.show()
# +--------------------+--------------------+--------------------+
# |                  c0|                  c1|                  c2|
# +--------------------+--------------------+--------------------+
# | -1.1854930781734352| -1.1854930781734352| -1.1854930781734352|
# |-0.24587658470592705|-0.24587658470592705|-0.24587658470592705|
# |  1.8039683668407596|  1.8039683668407596|  1.8039683668407596|
# |-0.18972856311959985|-0.18972856311959985|-0.18972856311959985|
# +--------------------+--------------------+--------------------+

# %% 
df = spark.range(22).withColumn('rand', f.rand(seed=42))
df = df.select(
    'id', 
    (f.col('rand') * 100).cast('integer').alias('rand'), 
    (f.rand(seed=42) * 10).cast('integer').alias('rand2'), 
    (f.rand(seed=42) * 10).cast('integer').alias('rand3'), 
)
df.show()

# %% f.cume_dist()
col='rand'
cdf_col = f.cume_dist().over(Window.orderBy(col))
df \
    .select(col, 'rand2') \
    .select(col, cdf_col.alias("cdf")) \
    .groupBy(col) \
    .agg(f.max("cdf").alias("cdf")) \
    .orderBy(col).show()
    

