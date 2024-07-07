#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
title: generating DataFrame
content:
    -
file:
    date: 2024-06-07
"""
# %%
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('sql_functions_01').getOrCreate()

from pyspark.sql import functions as f, DataFrame, types

# %%
spark.range(4).show()               # ~ range(4)
# +---+
# | id|
# +---+
# |  0|
# |  1|
# |  2|
# +---+

spark.range(0, 4, 1, 1).show()      # start, stop, step, nr of partitions
                                    # ~ range(0, 4, 1)  &  nr of partitions
spark.range(0, 4).show()

spark.range(0, 4, 2).show()
# +---+
# | id|
# +---+
# |  0|
# |  2|
# +---+

# %%
df = spark.createDataFrame(range(4), types.IntegerType())
df.show()
# +-----+
# |value|
# +-----+
# |    0|
# |    1|
# |    2|
# |    3|
# +-----+

df = spark.createDataFrame([1, 3, 3, 4], types.IntegerType())
df.show()
# +-----+
# |value|
# +-----+
# |    1|
# |    3|
# |    3|
# |    4|
# +-----+

df = spark.createDataFrame([(None, 2, ), (1, 3, )], ["e", "g"])
df.show()
# +----+---+
# |   e|  g|
# +----+---+
# |NULL|  2|
# |   1|  3|
# +----+---+

# %%
from itertools import product

spark.createDataFrame(list(product([1,2], [3,4,5], [8,9]))).show()
spark.createDataFrame(list(product([1,2], [3,4,5], [8,9])), ['a', 'b', 'c']).show()

# %%
