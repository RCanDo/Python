#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Spark DataFrame Basics
subtitle: GroupBy and Aggregate Functions
version: 1.0
type: course
keywords: [aggregating, DataFrame, big data, PySpark]
description: |
remarks:
todo:
sources:
    - title: Spark and Python for Big Data with PySpark
      chapter: DataFrames Basics
      section: Lecture 27 - GroupBy and Aggregate Functions
      pages:
      link: https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/learn/lecture/6688216#overview
      date: 2016
      authors:
          - fullname: Jose Portilla
            email:
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: 03-GroupBy_and_Aggregate_Functions.py
    path: ~/Works/Python/PySpark/Udemy/01-Spark_DataFrames/
    date: 2019-11-22
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""
#%%
cd ~/Works/Python/PySpark/Udemy/01-Spark_DataFrames/

#%% Creating a DataFrame
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local").appName("aggregates").getOrCreate()

df = spark.read.csv('sales_info.csv', inferSchema=True, header=True)
df.printSchema()
df.show()
df.count()

#%% GroupBy and Aggregate Functions
#%%

dfg = df.groupBy("Company")
dfg.mean().show()
dfg.avg().show()
dfg.count().show()
dfg.max().show()
dfg.min().show()
dfg.sum().show()

#%%
df.agg({'Sales':'max'}).show()
dfg.agg({'Sales':'max'}).show()

#%% Functions
from pyspark.sql.functions import countDistinct, avg, stddev

df.select(countDistinct("Sales")).show()
df.select(countDistinct("Sales").alias("Distinct sales")).show()
df.select(countDistinct("Sales").name("Distinct sales")).show()
df.select(avg("Sales")).show()
df.select(stddev("Sales")).show()

#%%
from pyspark.sql.functions import format_number

sales_stddev = df.select(stddev('Sales').alias('std'))
sales_stddev.show()

sales_stddev.select(format_number('std', 2)).show()

#%% Order By

df.orderBy("Sales").show()
df.orderBy(df["Sales"]).show()
df.orderBy(df["Sales"].desc()).show()
df["Sales"]
df["Sales"].desc()

#%%



#%%

