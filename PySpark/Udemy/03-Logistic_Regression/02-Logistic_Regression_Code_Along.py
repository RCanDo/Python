#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Logistic Regression
subtitle: Titnic example
version: 1.0
type: course
keywords: [pipelines, logistic regression, big data, PySpark]
description: |
remarks:
todo:
sources:
    - title: Spark and Python for Big Data with PySpark
      chapter: Logistic Regression
      section: Lecture 42 - Code along example
      link: https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/learn/lecture/9055686#overview
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
    date: 2019-12-27
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
spark = SparkSession.builder.appName("logreg_titanic").getOrCreate()

#%%
data_raw = spark.read.csv('titanic.csv', inferSchema=True, header=True)
data_raw.printSchema()
data_raw.columns
data_raw.count()  # 891

data = data_raw.select('Survived', 'Pclass', 'Sex', 'Age', 'SibSp',
                       'Parch', 'Fare', 'Embarked')
data = data.na.drop()
#%%
data.count()  # 712
data.printSchema()
data.show()

#%%
data_train, data_test = data.randomSplit([.7, .3])
n_train = data_train.count()  # 482
n_test = data_test.count()    # 230

#%%
from pyspark.ml.feature import VectorAssembler, VectorIndexer, \
                               OneHotEncoder, StringIndexer

gender_indexer = StringIndexer(inputCol='Sex', outputCol='SexIdx')
gender_encoder = OneHotEncoder(inputCol='SexIdx', outputCol='SexVec')

embark_indexer = StringIndexer(inputCol='Embarked', outputCol='EmbarkedIdx')
embark_encoder = OneHotEncoder(inputCol='EmbarkedIdx', outputCol='EmbarkedVec')

#%%
assembler = VectorAssembler(
        inputCols=['Pclass', 'SexVec', 'Age', 'SibSp',
                   'Parch', 'Fare', 'EmbarkedVec'],
        outputCol='features')

#%%
from pyspark.ml.classification import LogisticRegression
logreg = LogisticRegression(featuresCol='features', labelCol='Survived')

#%% Pipelines
from pyspark.ml import Pipeline

pipeline = Pipeline(stages=[gender_indexer, embark_indexer, 
                            gender_encoder, embark_encoder,
                            assembler, logreg])

#%%
model = pipeline.fit(data_train)
pred_test = model.transform(data_test)

type(pred_test)   # pyspark.sql.dataframe.DataFrame
pred_test.printSchema()
pred_test.select('Survived', 'prediction').show()


#%%
from pyspark.ml.evaluation import BinaryClassificationEvaluator

evaluator = BinaryClassificationEvaluator(rawPredictionCol='prediction', 
                                          labelCol='Survived')
AUC = evaluator.evaluate(pred_test)
AUC  # 0.7825239112266691

#%%



#%%

