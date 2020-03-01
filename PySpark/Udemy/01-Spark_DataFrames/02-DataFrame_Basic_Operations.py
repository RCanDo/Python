#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Spark DataFrame Basics
subtitle: Basic Operations
version: 1.0
type: course
keywords: [DataFrame, big data, PySpark]
description: |
remarks:
todo:
sources:
    - title: Spark and Python for Big Data with PySpark
      chapter: DataFrames Basics
      section: Lecture 26 - DataFrame Basic Operations
      pages:
      link: https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/learn/lecture/6675062#overview
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
    name: 02-DataFrame_Basic_Operations.py
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
spark = SparkSession.builder.master("local").appName("basic_ops").getOrCreate()

df = spark.read.csv('appl_stock.csv', inferSchema=True, header=True)
df.printSchema()

#%% Basic Operations
#%%

#%% Filtering Data

df.filter("Close<500").show()
df.filter("Close<500").select("Open").show()
df.filter("Close<500").select(["Open", "Close"]).show()
df.filter("Close<{}".format(500)).select(["Open", "Close"]).show()

#%%

df.filter(df['Close']<200).show()
df.filter((df['Close']<200) & (df['Open']>200)).show()
df.filter( df['Close']<200  &  df['Open']>200 ).show()  # ERROR!
df.filter((df['Close']<200) | (df['Open']>200)).show()
df.filter((df['Close']<200) & ~(df['Open']>200)).show()

df.select(['Low']).show()
df.filter(df['Low'] == 197.16).show()

#%% Collecting results as Python objects
res = df.filter(df['Low'] == 197.16).collect()
type(res)      # list
res            # list of Rows !!!
type(res[0])   # pyspark.sql.types.Row

#%%
row = res[0]
row.asDict()

for item in row:
    print(item)


#%%



