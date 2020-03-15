#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: K-Means Clustering
subtitle: Clustering Code Along - Seeds types
version: 1.0
type: course
keywords: [k-means, clustering, Big Data, PySpark]
description: |
remarks:
todo:
sources:
    - title: Spark and Python for Big Data with PySpark
      chapter: K-Means Clustering
      section: Lecture 52 - Clustering Code Along
      link: https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/learn/lecture/7023934#announcements
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
    name: 02-Clustering_Code_Along.py
    path: ~/Works/Python/PySpark/Udemy/05-Clustering/
    date: 2020-03-02
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""

#%%
cd ~/Works/Python/PySpark/Udemy/05-Clustering/

#%%
from pyspark.sql import SparkSession
spark = SparkSession.builder.master('local').appName('seeds').getOrCreate()

#%%
data_raw = spark.read.csv("seeds_dataset.csv", header=True, inferSchema=True)
data_raw.count()       # 210
data_raw.printSchema()
data_raw.show()

#%% 
from pyspark.ml.feature import VectorAssembler

assembler = VectorAssembler(outputCol='featuresUnscaled',
                            inputCols=data_raw.columns)

#%%
from pyspark.ml.feature import StandardScaler
scaler = StandardScaler(inputCol="featuresUnscaled", outputCol="features",
                        withStd=True, withMean=False)

#%%
from pyspark.ml import Transformer

class ColumnSelector(Transformer):
    
    def __init__(self, *args):
        super().__init__()
        self.args = args
    
    def transform(self, df):
        return df[[*self.args]]
    
selector = ColumnSelector('features')

#%%
from pyspark.ml.clustering import KMeans

est2 = KMeans(featuresCol='features', predictionCol='pred2', k=2, seed=1)
est3 = KMeans(featuresCol='features', predictionCol='pred3', k=3, seed=1)

#%%
from pyspark.ml import Pipeline

pipeline = Pipeline(stages=[assembler, scaler, selector,
                            est2, est3])

#%%
result = pipeline.fit(data_raw).transform(data_raw)

result.show()

#%%
wssse2 = est2.computeCost(result)
print(wssse2)

wssse3 = est3.computeCost(result)
print(wssse3)

#%%



#%%


#%%


#%%


#%%