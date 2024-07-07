#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
title: pyspark.sql.functions examples of usage – 01
content:
    - ifnull
    - count()
    - cum_dist()
    - expr()
    - col(), column()
    - counting NULLs
    - f.col(...)..cast()
file:
    date: 2024-04-12
"""

# %%
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('sql_functions_01').getOrCreate()

from pyspark.sql import functions as f, DataFrame, types

# %%
# %% f.ifnull()
df = spark.createDataFrame([(None, 2, ), (1, 3, )], ["e", "g"])
df.show()
df.select(f.ifnull(df.e, f.lit(8))).show()
df.select(f.ifnull(df.e, 8)).show()
    # ! PySparkTypeError: [NOT_COLUMN_OR_STR] Argument `col` should be a Column or str, got int.
df.select(f.ifnull(df.e, 'g')).show()

# %% f.nullif()
df = spark.createDataFrame([(1, 2,), (1, 3,), (1, 1,)], ["e", "g"])
df.show()
df.withColumn('qq', f.nullif(df.e, df.g)).show()

df.withColumn('qq', f.nullif(f.col("e"), f.col("g")))  # ??? AnalysisException: Invalid call to dataType on unresolved object
df.withColumn('qq', f.nullif("e", "g"))  # ??? AnalysisException: Invalid call to dataType on unresolved object
df.select(f.col("e"), f.col("g")).show()  # ??? AnalysisException: Invalid call to dataType on unresolved object

df.withColumn('qq', f.nullif(df.g, f.lit(1))).show()

# %%
df.show()
df.withColumn('if', f.col("e") == f.col("g")).show()
df.withColumn('if', f.col("g") >= 2).show()
df.withColumn('if', (f.col("e") == f.col("g")).cast("integer")).show()

df.withColumn('qq', f.lit(1)).show()

# %%  f.count()
"""
https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.count.html
Aggregate function: returns the number of items in a group.
"""

df = spark.createDataFrame([(None,), ("a",), ("b",), ("c",)], schema=["alphabets"])
df.show()
# +---------+
# |alphabets|
# +---------+
# |     NULL|
# |        a|
# |        b|
# |        c|
# +---------+

df.select(f.count(f.expr("*")), f.count(df.alphabets)).show()
# +--------+----------------+
# |count(1)|count(alphabets)|
# +--------+----------------+
# |       4|               3|           #  (1)
# +--------+----------------+

# %% f.cum_dist()

from pyspark.sql import Window, types
df = spark.createDataFrame([1, 2, 3, 3, 4], types.IntegerType())
df.show()

w = Window.orderBy("value")
df.withColumn("cd", f.cume_dist().over(w)).show()

# %%  f.expr
"""
https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.expr.html
Parses the expression string into the column that it represents
"""
df.select(f.expr("*")).show()
# +---------+
# |alphabets|
# +---------+
# |     NULL|
# |        a|
# |        b|
# |        c|
# +---------+

df.select('alphabets', f.expr("*")).show()
# +---------+---------+
# |alphabets|alphabets|
# +---------+---------+
# |     NULL|     NULL|
# |        a|        a|
# |        b|        b|
# |        c|        c|
# +---------+---------+

df.select('alphabets', f.expr("*")).printSchema()
# root
#  |-- alphabets: string (nullable = true)
#  |-- alphabets: string (nullable = true)

# ??? so why (1) ???

df.select(f.count(f.expr("*"))).show()
# +--------+
# |count(1)|
# +--------+
# |       4|
# +--------+


# ###
df = spark.createDataFrame([["Alice"], ["Bob"]], ["name"])
df.select("name", f.expr("length(name)")).show()
# +-----+------------+
# | name|length(name)|
# +-----+------------+
# |Alice|           5|
# |  Bob|           3|
# +-----+------------+

# ###
dfc = spark.createDataFrame([["Alice", 101], ["Bob", 12], ["It", None]], ["name", "value"])

dfc.select(["name", f.expr("*")]).show()
# +-----+-----+-----+
# | name| name|value|
# +-----+-----+-----+
# |Alice|Alice|  101|
# |  Bob|  Bob|   12|
# |   It|   It| NULL|
# +-----+-----+-----+
dfc.select(["name", "value", f.expr("*")]).show()
# +-----+-----+-----+-----+
# | name|value| name|value|
# +-----+-----+-----+-----+
# |Alice|  101|Alice|  101|
# |  Bob|   12|  Bob|   12|
# |   It| NULL|   It| NULL|
# +-----+-----+-----+-----+

# !!!
dfc.select(["name", f.count("value"), f.count(f.expr("*"))]).show()
# ! AnalysisException: [MISSING_GROUP_BY] The query does not include a GROUP BY clause.
# Add GROUP BY or turn it into the window functions using OVER clauses.;
# Aggregate [name#241, count(value#242L) AS count(value)#351L, count(1) AS count(1)#352L]
# +- LogicalRDD [name#241, value#242L], false

dfc.select([f.count("name"), f.count("value"), f.count(f.expr("*"))]).show()
# +-----------+------------+--------+
# |count(name)|count(value)|count(1)|
# +-----------+------------+--------+
# |          3|           2|       3|
# +-----------+------------+--------+

# %%  f.col(), f.column()
"""
https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.col.html
Returns a Column based on the given column name.
"""
f.col('qq')
# Column<'qq'>

dfc = spark.createDataFrame([["Alice", 101], ["Bob", 12], ["It", None]], ["name", "value"])
dfc.show()
# +-----+-----+
# | name|value|
# +-----+-----+
# |Alice|  101|
# |  Bob|   12|
# |   It| NULL|
# +-----+-----+

dfc.select([f.col(c) for c in dfc.columns]).show()
# the same df

dfc.select(dfc.columns).show()
# the same !
# i.e. there is usually no deed for using f.col()

dfc.select([f.col(c).isNull() for c in dfc.columns]).show()
# +--------------+---------------+
# |(name IS NULL)|(value IS NULL)|
# +--------------+---------------+
# |         false|          false|
# |         false|          false|
# |         false|           true|
# +--------------+---------------+


# all the same:
dfc.filter(dfc['value'] > 100).show()
dfc.filter(f.col('value') > 100).show()
dfc.filter(f.col('value') > f.lit(100)).show()
dfc.filter("value > 100").show()
thresh = 100
dfc.filter(f"value > {thresh}").show()
# +-----+-----+
# | name|value|
# +-----+-----+
# |Alice|  101|
# +-----+-----+

# %% Counting NULLs

# 1. using  count() – which counts only non-NULL values of a variable (column)
# seems simple but needs reversing NULLs to non-NULLs and vice-versa
# so it's rather tricky
dfc.select([f.when(f.col(c).isNull(), c).alias(f'qq-{c}') for c in dfc.columns]).show()
# +-------+--------+
# |qq-name|qq-value|
# +-------+--------+
# |   NULL|    NULL|
# |   NULL|    NULL|
# |   NULL|   value|
# +-------+--------+

dfc.select([f.count(f.when(f.col(c).isNull(), c)).alias(f'qq-{c}') for c in dfc.columns]).show()
# +-------+--------+
# |qq-name|qq-value|
# +-------+--------+
# |      0|       1|
# +-------+--------+

# 2. !!! count_if() – most natural!
dfc.select([f.count_if(f.col(c).isNull()).alias(f'qq-{c}') for c in dfc.columns]).show()
# the same

# 3. sum() of `boolean` cast to `int`
dfc.select([f.sum(f.col(c).isNull().cast('int')).alias(f'qq-{c}') for c in dfc.columns]).show()
# +-------+--------+
# |qq-name|qq-value|
# +-------+--------+
# |      0|       1|
# +-------+--------+

# %%  .cast()
from pyspark.sql.types import StringType

df = spark.createDataFrame(
     [(2, "Alice", True), (5, "Bob", False)], ["age", "name", "bool"])
df.show()

df.select(df.age.cast("string").alias('ages')).collect()

df.select(df.age.cast(StringType()).alias('ages')).collect()

df.select(df.bool.cast('int')).collect()

# %%
