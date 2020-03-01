#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Spark DataFrame Basics
subtitle: Dates and Timestamps
version: 1.0
type: course
keywords: [aggregating, DataFrame, big data, PySpark]
description: |
remarks:
todo:
sources:
    - title: Spark and Python for Big Data with PySpark
      chapter: DataFrames Basics
      section: Lecture 29 - Dates and Timestamps
      pages:
      link: https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/learn/lecture/6688226#overview
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
    name: 04-Dates_and_Timestamps.py
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
spark = SparkSession.builder.master("local").appName("dates").getOrCreate()

df = spark.read.csv('appl_stock.csv', inferSchema=True, header=True)
df.count()  # 1762

df.printSchema()
df.show()
df.select('Date').show()
df.select('Date').show(n=40)
df['Date']

#%% Dates and Timestamps
#%%
from pyspark.sql.functions import format_number, dayofmonth, hour, dayofyear, \
    month, year, weekofyear, date_format

#%%

df.select(dayofmonth(df['Date'])).show()
df.select(dayofmonth(df['Date']).alias('day of month')).show()
df.select(dayofyear(df['Date']).alias('day of year')).show()
df.select(month(df['Date']).alias('month')).show()

df.select(hour(df['Date'])).show()

df.select(year(df['Date']).alias('year')).show()

#%%
df.withColumn("Year", year(df['Date'])).show()

newdf = df.withColumn("Year", year(df["Date"]))
newdf_mean = newdf.groupBy("Year").mean()
newdf_mean.show()

newdf_mean['avg(Close)']
newdf_mean['avg(Close)'].show()   #! TypeError: 'Column' object is not callable
# BUT
newdf_mean[['avg(Close)']].show()
newdf_mean[['Year', 'avg(Year)','avg(Close)', 'avg(Open)']].show()

#%% add aliases and format_number

meandf = newdf_mean[['Year', 'avg(Open)', 'avg(Close)', 'avg(Volume)']]
meandf = meandf.select('Year', \
                       format_number('avg(Open)', 2).alias('mean open'), \
                       format_number('avg(Close)', 2).alias('mean close'), \
                       format_number('avg(Volume)', 2).alias('mean volume'), \
                       )
meandf.show()

#%%