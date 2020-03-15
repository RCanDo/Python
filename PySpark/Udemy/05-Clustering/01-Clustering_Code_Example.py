#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: K-Means Clustering
subtitle: Documentation Example
version: 1.0
type: course
keywords: [k-means, clustering, Big Data, PySpark]
description: |
remarks:
todo:
sources:
    - title: Spark and Python for Big Data with PySpark
      chapter: K-Means Clustering
      section: Lecture 51 - K-Means Clustering Documentation Example
      link: https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/learn/lecture/7023942#announcements
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
    name: 01-Clustering_Code_Example.py
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
spark = SparkSession.builder.master('local').appName('clustering_example').getOrCreate()

#%%
data_raw = spark.read.format("libsvm").load("sample_kmeans_data.txt")
data_raw.count()     # 6
data_raw.printSchema()
data_raw.show(truncate=False)

# data ready to analyse so
data = data_raw

#%%
from pyspark.ml.clustering import KMeans

est = KMeans().setK(2).setSeed(1)
mod = est.fit(data)

#%% Within Set Sum Of Squared Errors
wssse = mod.computeCost(data)
print("Within Set Sum of Squared Errors = {:2.3f}".format(wssse)) 

#%%
mod.clusterCenters()

#%%
dir(mod.summary)
mod.summary.cluster.show()
mod.summary.clusterSizes
mod.summary.predictions.show()
...
mod.summary.trainingCost  # == wsssw == mod.comuteCost(data)
# this is for training data             this is for any data

#%%
mod.transform(data).show()

#%%


