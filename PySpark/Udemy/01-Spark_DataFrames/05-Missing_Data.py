#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Spark DataFrame Basics
subtitle: Missing Data
version: 1.0
type: course
keywords: [aggregating, DataFrame, big data, PySpark]
description: |
remarks:
todo:
sources:
    - title: Spark and Python for Big Data with PySpark
      chapter: DataFrames Basics
      section: Lecture 28 - Missing Data
      pages:
      link: https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/learn/lecture/6688224#overview
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
    name: 05-Missing_Data.py
    path: ~/Works/Python/PySpark/Udemy/01-Spark_DataFrames/
    date: 2019-11-23
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
sess = SparkSession.builder.master("local").appName("missingdata").getOrCreate()

df = spark.read.csv('ContainsNull.csv', inferSchema=True, header=True)
df.count()
df.printSchema()
df.show()

#%% Missing Data
#%%

#%% Drop the missing data
#%%

# drop any row containing null
df.na.drop().show()
df.na.drop(how='any').show()

# drop only rows with all nulls
df.na.drop(how='all').show()

# leave only when at least 2 non-null values
df.na.drop(thresh=2).show()

#%%
df.na.drop(subset=['Sales']).show()

#%% Fill the missing values
"""
We can also fill the missing values with new values.
If you have multiple nulls across multiple data types,
Spark is actually smart enough to match up the data types.
"""
df.na.fill('UNKNOWN').show()
df.na.fill(-1).show()
df.na.fill('UNKNOWN').na.fill(-1).show()

# you may specify what columns you want to fill with the subset parameter
df.na.fill('unknown', subset=['Name']).show()

# arguments position is convienient
df.na.fill('unknown', ['Name']).show()

#%% filling with mean value:
from pyspark.sql.functions import mean
df.select(mean(df.Sales))
df.select(mean(df.Sales)).show()
df.select(mean(df.Sales)).collect()  # list of rows ~= .head(n)
df.select(mean(df.Sales)).collect()[0]
df.select(mean(df.Sales)).collect()[0][0]
# equiv
df.select(mean(df.Sales)).head()[0]

# again
mean_sales = df.select(mean(df.Sales)).head()[0]
mean_sales
df.na.fill(mean_sales, ['Sales']).show()

#%%
