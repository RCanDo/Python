#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Logistic Regression
subtitle: Example
version: 1.0
type: course
keywords: [logistic regression, big data, PySpark]
description: |
remarks:
todo:
sources:
    - title: Spark and Python for Big Data with PySpark
      chapter: Logistic Regression
      section: Lecture 41 - Example
      link: https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/learn/lecture/6688268#overview
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
    name: 02-Logistic_Regression_Code_Along.py
    path: ~/Works/Python/PySpark/Udemy/03-Logistic_Regression/
    date: 2019-12-26
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""


#%%
cd ~/Works/Python/PySpark/Udemy/03-Logistic_Regression/

#%%
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local").appName("logistic_example").getOrCreate()

from pyspark.ml.classification import LogisticRegression

#%%
data_raw = spark.read.format("libsvm").load("sample_libsvm_data.txt")

data_raw.printSchema()
data_raw.show()
data_raw.describe().show()
data_raw.head()[1]    # SparseVector(692, {...})

#%%
data_train, data_test = data_raw.randomSplit([.7, .3])
n_train = data_train.count()
n_test = data_test.count()

#%%
logreg = LogisticRegression()

#%%
model = logreg.fit(data_train)

model.coefficients
model.intercept

model.summary.accuracy   # 1
model.summary.areaUnderROC  # 1

model.summary.predictions.show()
probs = model.summary.predictions[['probability']].collect()

zeros = [probs[k][0][0] for k in range(n_train)]
ones = [probs[k][0][1] for k in range(n_train)]

import matplotlib.pyplot as plt
plt.scatter(range(n_train), zeros)
plt.scatter(range(n_train), ones)

#%% evaluation

eval_test = model.evaluate(data_test)
eval_test
eval_test.predictions.show()

data_test_yyhat = eval_test.predictions.select('label', 'prediction')
data_test_yyhat.show(n=40)

#%%
"""
https://spark.apache.org/docs/latest/api/python/pyspark.ml.html#pyspark.ml.evaluation.MulticlassClassificationEvaluator
https://spark.apache.org/docs/latest/api/python/pyspark.ml.html#pyspark.ml.evaluation.BinaryClassificationEvaluator
"""
# from pyspark.mllib.evaluation import MulticlassMetrics
from pyspark.ml.evaluation import BinaryClassificationEvaluator, \
                                  MulticlassClassificationEvaluator

eval_bin = BinaryClassificationEvaluator(rawPredictionCol='prediction',
                                         labelCol='label')

eval_multi = MulticlassClassificationEvaluator(predictionCol='prediction',
                                               labelCol='label',
                                               metricName='accuracy')

#%%
eval_bin_eval = eval_bin.evaluate(data_test_yyhat)
eval_bin_eval     # 0.9615384615384616

eval_multi_eval = eval_multi.evaluate(data_test_yyhat)
eval_multi_eval   # 0.967741935483871

#%%

#%%