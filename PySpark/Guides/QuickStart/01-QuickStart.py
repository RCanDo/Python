#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: First simple Spark app
version: 1.0
type: guide
keywords: [big data, PySpark]
description: |
remarks:
todo:
sources:
    - title: Quick Start
      chapter: Self-Contained Applications
      link: https://spark.apache.org/docs/latest/quick-start.html
      date: 2020
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: True     # if the file is intended to be run in a terminal
    name: 01-QuickStart.py
    path: ~/Works/Python/PySpark/Guides/QuickStart/
    date: 2020-01-16
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""

#%% do it now! 
#! after initializing session changing directory has no effect
# cd ~/Works/Python/PySpark/Guides/QuickStart/

#%%
from pyspark.conf import SparkConf
dir(SparkConf())
SparkConf().getAll()
# ...

#%% 
from pyspark.sql import SparkSession
spark = SparkSession.builder \
        .master('local') \
        .appName("SimpleApp").getOrCreate() 
                            #.config("spark.some.config.option", "some-value").getOrCreate() 
        
type(spark)   # pyspark.sql.session.SparkSession
# https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.SparkSession


#%% Creating a DataFrame

txtFile = "some_file.txt"
data = spark.read.text(txtFile).cache()

#%%
type(data)  # pyspark.sql.dataframe.DataFrame
data.show()
data.columns
data.printSchema()
data.describe().show()

data.select('value').show()
data.select('value').show(99, False)
data['value']
data.value
data.select(data['value']).show()
data.select(data.value).show()


#%%
nrows = data.count()
print("Number of rows: %i" % nrows)

#%%
firstrow = data.first()  # == .head()
print(firstrow)
print(firstrow.value)
dir(firstrow)
firstrow.index(1)   #! ???
firstrow.count(0)   # ?
firstrow.asDict()

#%%
linesWithSpark = data.filter(data.value.contains("Spark"))
type(linesWithSpark)  # pyspark.sql.dataframe.DataFrame

for r in linesWithSpark.collect():
    print(r)
    print(r.value)
    print('-')
    
nspark = linesWithSpark.count()
print("Lines with Spark: %i" %nspark)

#%%
import pyspark.sql.functions as psf

d2 = data.select(psf.size(psf.split(data.value, '\s+')).name("numWordsInLine"))
# d2.show(100)
maxNumWordsInLine = d2.agg(psf.max(psf.col("numWordsInLine"))).head()[0]
print("Maximum number of words in one line: %i" %maxNumWordsInLine)

#%%
d2 = data.select(psf.explode(psf.split(data.value, '\s+')).alias("word"))
# d2.show(100)
d2.groupBy('word').count().show()      # DataFrame
d2.groupBy('word').count().collect()   # list of rows
ll = [list(row.asDict().values()) for row in d2.groupBy('word').count().collect()]
for l in ll:
    print("{}: {}".format(*l))
    
#%%


#%%
numAs = data.filter(data.value.contains('a')).count()
numBs = data.filter(data.value.contains('b')).count()

print("Lines with a: %i; lines with b: %i" % (numAs, numBs))

spark.stop()

#%%



#%%
