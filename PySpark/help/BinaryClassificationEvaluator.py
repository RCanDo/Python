#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 11:41:31 2019
https://spark.apache.org/docs/latest/api/python/pyspark.ml.html#pyspark.ml.evaluation.BinaryClassificationEvaluator
@author: arek
"""

#%%

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('binaryClassEval').getOrCreate()

from pyspark.ml.linalg import Vectors
scoreAndLabels = map(lambda x: (Vectors.dense([1. - x[0], x[0]]), x[1]),
                     [(0.1, 0.0), (0.1, 1.0), (0.4, 0.0), (0.6, 0.0), (0.6, 1.0), (0.6, 1.0), (0.8, 1.0)])
# list(scoreAndLabels)

#%%
data = spark.createDataFrame(scoreAndLabels, ['raw', 'label'])
data.show()


