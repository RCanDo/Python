#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Spark DataFrame Basics
subtitle: Introduction
version: 1.0
type: course
keywords: [DataFrame, big data, PySpark]
description: |
remarks:
todo:
sources:
    - title: Spark and Python for Big Data with PySpark
      chapter: DataFrames Basics
      section: Lecture 23 - Introduction to Spark DataFrames
      pages:
      link: https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/learn/lecture/6688214#overview
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
    name: 01-DataFrame_Basics.py
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

#%%
from pyspark.conf import SparkConf
dir(SparkConf())
SparkConf().getAll()
# ...

#%% 
from pyspark.sql import SparkSession
spark = SparkSession.builder \
        .master('local') \
        .appName("basics").getOrCreate()
                         #.config("spark.some.config.option", "some-value").getOrCreate()
type(spark)   # pyspark.sql.session.SparkSession
# https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.SparkSession

#%% Creating a DataFrame
df = spark.read.json('people.json')
type(df)  # pyspark.sql.dataframe.DataFrame
# https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame

#%%
df.show()
df.printSchema()
df.columns
df.describe().show()

#%%
from pyspark.sql.types import StructField, StringType, IntegerType, StructType

# StructField(name, type, nullable)
data_schema = [StructField("age", IntegerType(), True),
               StructField("name", StringType(), True)]
structure = StructType(fields=data_schema)
df = spark.read.json('people.json', schema=structure)

df.printSchema()

#%% Grabbing The Data

df['age']
type(df['age'])
df.select('age')
type(df.select('age'))   # pyspark.sql.dataframe.DataFrame

df.select('age').show()
df.head()    # row
df.head(1)   # list of rows
df.head(2)

df.first()   # = .head()
df.first(2)   #! Error

df.select(['age', 'name'])   # pyspark.sql.dataframe.DataFrame
df.select(['age', 'name']).show()

#%% Creating new columns
df.withColumn('newage', df['age']).show()
df.show()  # not changed

# simple rename
df.withColumnRenamed('age', 'supernewage').show()
df.show()

#%%
df.withColumn('doubleage', df['age']*2).show()
df.withColumn('add_one_age', df['age']+1).show()

df2 = df.withColumn('half_age', df['age']/2)
df2
df2.printSchema()
df2.show()

#%% Using SQL

# Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView('people')

query01 = spark.sql("SELECT * FROM people")
query01
query01.show()

query02 = spark.sql("SELECT * FROM people WHERE age>20")
query02.show()

#%% ...
dfc = df.cube('name', 'age')
dfc.show()  #! AttributeError: 'GroupedData' object has no attribute 'show'
dfc.count().show()

#%%

