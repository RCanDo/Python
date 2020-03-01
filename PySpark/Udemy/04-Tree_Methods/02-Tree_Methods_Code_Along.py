#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Decision Trees And Random Forest
subtitle: Tree Methods Code Along
version: 1.0
type: course
keywords: [Gradient Boosted Trees, Decision Trees, Random Forest, Big Data, PySpark]
description: |
remarks:
todo:
sources:
    - title: Spark and Python for Big Data with PySpark
      chapter: Decision Trees And Random Forest
      section: Lecture 47 - Tree Methods Code Along
      link: https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/learn/lecture/7023954#announcements
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
    name: 02-Tree_Methods_Code_Along.py
    path: ~/Works/Python/PySpark/Udemy/04-Tree_Methods/
    date: 2020-02-28
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""

#%%
cd ~/Works/Python/PySpark/Udemy/04-Tree_Methods/

#%%
from pyspark.sql import SparkSession
spark = SparkSession.builder.master('local').appName('trees_code_along').getOrCreate()

#%%
data_raw = spark.read.format('csv').load("College.csv", header=True, inferSchema=True)
data_raw.printSchema()
data_raw.head().asDict()

data_raw[['Private']].groupBy('Private').count().show()

#%%
from pyspark.ml.feature import StringIndexer

private_idx = StringIndexer(inputCol='Private', outputCol='PrivateIdx')
#data_raw = private_idx.fit(data_raw).transform(data_raw)

#%%
#from pyspark.ml.linalg import Vector
from pyspark.ml.feature import VectorAssembler

data_raw.columns
assembler = VectorAssembler(outputCol='features',
                            inputCols=data_raw.columns[2:])

data_raw = assembler.transform(data_raw)

#%%
from pyspark.ml import Transformer

class SelectCols(Transformer):
    
    def __init__(self, *args):
        super().__init__()
        self.args = args
        
    def transform(self, df):
        return df[[*self.args]]

selector = SelectCols('features', 'PrivateIdx')

#%% 
from pyspark.ml import Pipeline
pipeline1 = Pipeline(stages=[private_idx, assembler, selector])

data = pipeline1.fit(data_raw).transform(data_raw)

data.printSchema()
data.count()   # 777
data.show(10)
data[['PrivateIdx']].groupBy('PrivateIdx').count().show()

#%%
data_train, data_test = data.randomSplit([.7, .3])
data_train.count()  # 538
data_test.count()   # 239

#%%
#%%
from pyspark.ml.classification import DecisionTreeClassifier, \
                                      RandomForestClassifier, \
                                      GBTClassifier

#%%
est_dt = DecisionTreeClassifier(featuresCol='features', labelCol='PrivateIdx')
est_rf = RandomForestClassifier(featuresCol='features', labelCol='PrivateIdx')
est_gb = GBTClassifier(featuresCol='features', labelCol='PrivateIdx')

#%%
model_dt = est_dt.fit(data_train)
model_rf = est_rf.fit(data_train)
model_gb = est_gb.fit(data_train)

#%%
pred_dt = model_dt.transform(data_train)
pred_rf = model_rf.transform(data_train)
pred_gb = model_gb.transform(data_train)

pred_dt.printSchema()
pred_rf.printSchema()
pred_gb.printSchema()

#%%
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

evaluator = MulticlassClassificationEvaluator(labelCol='PrivateIdx',
                                              predictionCol='prediction',
                                              metricName='accuracy')

#%%
evaluator.evaluate(pred_dt)   # 0.9814
evaluator.evaluate(pred_rf)   # 0.9777
evaluator.evaluate(pred_gb)   # 1.

#%%
#%% ? how to turn it into pipeline ??? three branches




