#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Decision Trees And Random Forest
subtitle: Tree Methods Documentation Example
version: 1.0
type: course
keywords: [Gradient Boosted Trees, Decision Trees, Random Forest, Big Data, PySpark]
description: |
remarks:
todo:
sources:
    - title: Spark and Python for Big Data with PySpark
      chapter: Decision Trees And Random Forest
      section: Lecture 46 - Tree Methods Documentation Example
      link: https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/learn/lecture/7023956#announcements
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
    name: 01-Tree_Methods_Doc_Example.py
    path: ~/Works/Python/PySpark/Udemy/04-Tree_Methods/
    date: 2020-02-27
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
spark = SparkSession.builder.master('local').appName('trees_doc_example').getOrCreate()

#%%
data_raw = spark.read.format('libsvm').load('sample_libsvm_data.txt')

data_raw.count()  # 100
data_raw.printSchema()
data_raw.head()

data_raw.groupBy('label').count().show()  # 

#%%
data_train, data_test = data_raw.randomSplit([.7, .3])

#%%
from pyspark.ml.classification import RandomForestClassifier

rfc = RandomForestClassifier()
model = rfc.fit(data_train)

#%% will need this later -- special meaning for RF model
model.featureImportances
# for this example rather useless -- too many enigmatic variables

#%%
pred_train = model.transform(data_train)
pred_train.printSchema()
pred_train.show()

#%%
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

evaluator = MulticlassClassificationEvaluator(labelCol='label', 
                                              predictionCol='prediction',
                                              metricName='accuracy')

eval_train = evaluator.evaluate(pred_train)
eval_train   # 1.0

#%%
pred_test = model.transform(data_test)
eval_test = evaluator.evaluate(pred_test)
eval_test    # 1.0

#%%
#%% Gradient Boosted Trees
#%%
"""
Gradient-boosted trees (GBTs) are a popular classification and regression method 
using ensembles of decision trees. 
More information about the spark.ml implementation can be found further 
in the section on GBTs.. 
For more information on the algorithm itself, please see the spark.mllib documentation 
on GBTs.
Luckily Spark makes very easy to use, basically just an import switch:
"""
#%%

from pyspark.ml.classification import GBTClassifier

gbt = GBTClassifier()
model = gbt.fit(data_train)

pred_train = model.transform(data_train)
pred_train.printSchema()

#%%
evaluator.evaluate(pred_train)   # 1.0
   
#%%
pred_test = model.transform(data_test)
evaluator.evaluate(pred_test)    # .0964


#%%



#%%



#%%