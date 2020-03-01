#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Streaming Word Count
subtitle:
version: 1.0
type: guide
keywords: [streaming, big data, PySpark]
description: |
remarks:
    - in one terminal run `nc -lk 9999`
    - in second run `spark-submit this_script.py localhost 9999`
todo:
sources:
    - title: Structured Streaming Programming Guide
      link: https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html
    - chapter: Quick Example
      link: https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#quick-example
      date: 2020
      usage: |
          not only copy
file:
    usage:
        interactive: False   # if the file is intended to be run interactively e.g. in Spyder
        terminal: True     # if the file is intended to be run in a terminal
    name: 01-StructuredNetworkWordCount.py
    path: ~/Works/Python/PySpark/Guides/Streaming/
    date: 2020-02-29
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""

#%%
cd ~/Works/Python/PySpark/Guides/Streaming/

#%%
from pyspark.sql import SparkSession
spark = SparkSession.builder.master('local') \
        .appName('StructuredNetworkWordCount').getOrCreate()

#%% Create DataFrame representing the stream of input lines 
# from connection to localhost:9999

lines = spark.readStream.format('socket') \
        .option('host', 'localhost') \
        .option('port', 9999) \
        .load()

# type(lines)    # DataFrame
# lines.show()   #! AnalysisException: 
#                   'Queries with streaming sources must be executed with 
#                    writeStream.start();;\nsocket'

#%% Split the lines into words
from pyspark.sql.functions import split, explode

words = lines.select(explode(split(lines.value, " ")).alias('word'))

#%% Generate running word count
wordCounts = words.groupBy('word').count()

#%% Start running the query that prints the running counts to the console
query = wordCounts.writeStream \
                  .outputMode('complete') \
                  .format('console') \
                  .start()
                  
query.awaitTermination()

#%%

#%%


#%%
