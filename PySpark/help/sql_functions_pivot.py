#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
title: pyspark.sql.functions examples of usage – 02
content:
    - 
file:
    date: 2024-05-31
"""

# %%
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('sql_functions_01').getOrCreate()

from pyspark.sql import functions as f, DataFrame, types

# %%
from pyspark.sql import Row
df1 = spark.createDataFrame([
    Row(course="dotNET", year=2012, earnings=10000),
    Row(course="Java", year=2012, earnings=20000),
    Row(course="dotNET", year=2012, earnings=5000),
    Row(course="dotNET", year=2013, earnings=48000),
    Row(course="Java", year=2013, earnings=30000),
])
df1.show()

df2 = spark.createDataFrame([
    Row(training="expert", sales=Row(course="dotNET", year=2012, earnings=10000)),
    Row(training="junior", sales=Row(course="Java", year=2012, earnings=20000)),
    Row(training="expert", sales=Row(course="dotNET", year=2012, earnings=5000)),
    Row(training="junior", sales=Row(course="dotNET", year=2013, earnings=48000)),
    Row(training="expert", sales=Row(course="Java", year=2013, earnings=30000)),
])  
df2.show()

# Compute the sum of earnings for each year by course with each course as a separate column
df1.groupBy("year").pivot("course", ["dotNET", "Java"]).sum("earnings").show()
# +----+------+-----+
# |year|dotNET| Java|
# +----+------+-----+
# |2012| 15000|20000|
# |2013| 48000|30000|
# +----+------+-----+

# Or without specifying column values (less efficient)
df1.groupBy("year").pivot("course").sum("earnings").show()
# +----+-----+------+
# |year| Java|dotNET|
# +----+-----+------+
# |2012|20000| 15000|
# |2013|30000| 48000|
# +----+-----+------+

df2.groupBy("sales.year").pivot("sales.course").sum("sales.earnings").show()
# +----+-----+------+
# |year| Java|dotNET|
# +----+-----+------+
# |2012|20000| 15000|
# |2013|30000| 48000|
# +----+-----+------+


# %%
cm0 = spark.createDataFrame([
    Row(real=True, pred=True, count=10000),
    Row(real=True, pred=False, count=100),
    Row(real=False, pred=True, count=200),
    Row(real=False, pred=False, count=20000),
])
cm0.show()

cm0.groupby("real").pivot("pred").sum("count").show()
# +-----+-----+-----+
# | real|false| true|
# +-----+-----+-----+
# | true|  100|10000|
# |false|20000|  200|
# +-----+-----+-----+

cm0.groupby("real").pivot("pred", ['true', 'false']).sum("count").show()
# +-----+-----+-----+
# | real| true|false|
# +-----+-----+-----+
# | true|10000|  100|
# |false|  200|20000|
# +-----+-----+-----+

# %%
cm0.withColumn('cm_cell', 
    f.when(f.col("real") == f.col("pred"),
        f.when(f.col("real"), "TP") \
        .otherwise("TN")
    ) \
    .otherwise(
        f.when(f.col("real"), "FN") \
        .otherwise("FP")
    )
).show()

# %%    
from typing import Union

def binary_product(
        df, col1: str, col2: str, 
        product_name: str = "bin_prod",
        tt: Union[str, int] = 'TP',
        tf: Union[str, int] = 'FN',
        ft: Union[str, int] = 'FP',
        ff: Union[str, int] = 'TN',
) -> DataFrame:
    dfp = df.withColumn(product_name, 
        f.when(f.col(col1) == f.col(col2),
            f.when(f.col(col1), tt) \
            .otherwise(ff)
        ) \
        .otherwise(
            f.when(f.col(col1), tf) \
            .otherwise(ft)
        )
    )
    return dfp


# %%

binary_product(cm0, 'real', 'pred', 'cm').show()


# %%














