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

data['value']
data.value
type(data.value)    # pyspark.sql.column.Column
data.value.show()   # ! TypeError: 'Column' object is not callable

type(data.select('value'))   # pyspark.sql.dataframe.DataFrame
data.select('value').show()  # OK
data.select('value').show(99, False)


data.select(data['value']).show()
data.select(data.value).show()

data.count()    # 26
data.collect()  # list of rows
# [Row(value='This is some file'),
#  Row(value='created only as an example'),
#  Row(value='to present abilities'),
#  Row(value='of PySpark package'),
#  ...

#%%
firstrow = data.first()  # == .head()
firstrow
type(firstrow)      # pyspark.sql.types.Row
dir(firstrow)

firstrow.value      # although it's not in dir() !
firstrow['value']   # the same

firstrow.index(1)   #! ???  ValueError: tuple.index(x): x not in tuple
firstrow.count(0)   # 0
firstrow.count('This is some file')   # 1
firstrow.asDict()   # {'value': 'This is some file'}

#%%
linesWithSpark = data.filter(data.value.contains("Spark"))
type(linesWithSpark)  # pyspark.sql.dataframe.DataFrame

for r in linesWithSpark.collect():
    print(r)
    print(r.value)
    print('-')

linesWithSpark.count()      # 3

#%%
import pyspark.sql.functions as psf

psf.split(data.value, '\s+')    # Column<'split(value, \s+, -1)'>
psf.split(data.value, '\s+').show()     # ! TypeError: 'Column' object is not callable

data.select(psf.split(data.value, '\s+')).show()    # OK
data.select(psf.size(psf.split(data.value, '\s+'))).show()

d2 = data.select(psf.size(psf.split(data.value, '\s+')).name("numWordsInLine"))
d2.show(100)

psf.col("numWordsInLine")   # Column<'numWordsInLine'>
psf.col("numWordsInLine").count()
data.select(psf.col("numWordsInLine")).show()   # ! AnalysisException: [UNRESOLVED_COLUMN.WITH_SUGGESTION] A column or function parameter with name `numWordsInLine` cannot be resolved.
d2.select(psf.col("numWordsInLine")).show()     # OK
d2.show()   # the same stuff
d2.select(psf.max(psf.col("numWordsInLine"))).show()
# +-------------------+
# |max(numWordsInLine)|
# +-------------------+
# |                  7|
# +-------------------+
d2.agg(psf.max(psf.col("numWordsInLine"))).show()   # the same

d2.agg(psf.max(psf.col("numWordsInLine"))).head()       # Row(max(numWordsInLine)=7)    !
type(d2.agg(psf.max(psf.col("numWordsInLine"))).head()) # pyspark.sql.types.Row
d2.agg(psf.max(psf.col("numWordsInLine"))).head()['max(numWordsInLine)']    # 7
d2.agg(psf.max(psf.col("numWordsInLine"))).head()[0]    # 7
d2.agg(psf.max(psf.col("numWordsInLine"))).head().asDict()      # {'max(numWordsInLine)': 7}

#%%
d2 = data.select(psf.explode(psf.split(data.value, '\s+')).alias("word"))
d2.show(100)

d2 = data.select(psf.explode(psf.split(data.value, '\s+')).name("word"))     # the same
d2.show(100)

d2.groupBy('word').count().show()      # DataFrame
d2.groupBy('word').count().collect()   # list of rows
# [Row(word='some', count=1),
#  Row(word='...', count=1),
#  Row(word='present', count=1),
#  Row(word='not', count=1),
#  ...

ll = [list(row.asDict().values()) for row in d2.groupBy('word').count().collect()]
ll

#%%
data.filter(data.value.contains('a')).count()   # 15
data.filter(data.value.contains('a')).show()

data.filter(data.value.contains('b')).count()   # 3
data.filter(data.value.contains('b')).show()

# %%
type(d2.groupBy('word').count()['count'])       # pyspark.sql.column.Column
dir(d2.groupBy('word').count()['count'])

d2.filter(d2.groupBy('word').count()['count'].contains(2)).show()
# !? AnalysisException: [MISSING_ATTRIBUTES.RESOLVED_ATTRIBUTE_MISSING_FROM_INPUT] Resolved attribute(s) "count" missing from "word"

spark.stop()

#%%



#%%
