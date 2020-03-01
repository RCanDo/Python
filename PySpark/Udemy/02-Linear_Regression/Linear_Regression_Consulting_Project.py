#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Linear Regression
subtitle: Predicting crew number for Hyunday ships
version: 1.0
type: course
keywords: [linear regression, big data, PySpark]
description: |
remarks:
todo:
sources:
    - title: Spark and Python for Big Data with PySpark
      chapter: Linear Regression
      section: Lecture 38 - Consulting project
      pages:
      link: https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/learn/lecture/6688264#overview
      date: 2016
      authors:
          - fullname: Jose Portilla
            email:
      usage: |
          not only copy
    - link: https://spark.apache.org/docs/latest/ml-classification-regression.html#regression
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: Linear_Regression_Consulting_Project.py
    path: ~/Works/Python/PySpark/Udemy/02-Linear_Regression/
    date: 2019-12-22
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""

#%%
cd ~/Works/Python/PySpark/Udemy/02-Linear_Regression/

#%%
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("project").getOrCreate()

data_raw = spark.read.csv("cruise_ship_info.csv", inferSchema=True, header=True)
#%%
data_raw.count()
data_raw.printSchema()
data_raw.describe().show()

#%%

#!!! EDA in Spark!!!
dd = data_raw[['Cruise_line']].collect()
dd
ll = [list(k.asDict().values())[0] for k in dd]
ll

# Counter
from collections import Counter
Counter(ll)

# Pandas
pdf = data_raw.toPandas()
pdf
pdfg = pdf.groupby('Cruise_line')
pdfg.sum()
pdfg.count()

# native
data_raw_g = data_raw.groupBy("Cruise_line")
data_raw_g.count().show()
data_raw_g.count().orderBy('count').show()

#%%
from pyspark.ml.feature import StringIndexer

indexer = StringIndexer(inputCol="Cruise_line", outputCol="cruise_idx")
data = indexer.fit(data_raw).transform(data_raw)
data.show()

#%%
from pyspark.ml.feature import VectorAssembler

data.columns
assembler = VectorAssembler(inputCols=['Age', 'Tonnage', 'passengers',
                                        'length', 'cabins', 'passenger_density',
                                        'cruise_idx'],
                            outputCol="features")

data2 = assembler.transform(data)
data2.printSchema()

#%%
data_all = data2.select('features', 'crew')
data_all.show()

data_train, data_test = data_all.randomSplit([.7, .3])
n_train = data_train.count()  # 117
n_test = data_test.count()    # 42

#%%
from pyspark.ml.regression import LinearRegression

lr = LinearRegression(featuresCol="features", labelCol="crew",
                      predictionCol="prediction")

#%%
mod0 = lr.fit(data_train)
dir(mod0)
mod0.coefficients
mod0.intercept

dir(mod0.summary)                                                          #!!!
mod0.featuresCol
mod0.summary.r2  # 0.9371511216685178
mod0.summary.meanSquaredError # 0.7927998697427192
mod0.summary.rootMeanSquaredError # 0.8903930984361453
mod0.numInstances  # AttributeError: 'LinearRegressionModel' object has no attribute 'numInstances'
mod0.summary.pValues
mod0.summary.tValues
mod0.summary.coefficientStandardErrors

#%% the model is really good;
# but it's not so strange in iew of
from pyspark.sql.functions import corr

data_raw.select(corr('crew', 'passengers')).show()  # 0.9152341306065384
data_raw.select(corr('crew', 'cabins')).show()      # 0.9508226063578497

#%%

mod0.summary.residuals.show()
mod0.summary.predictions.show()
mod0.summary.numInstances  # 117

#%%
import matplotlib.pyplot as plt
plt.scatter(range(n_train), mod0.summary.residuals.collect())

plt.figure()
plt.scatter(mod0.summary.predictions[['crew']].collect(),
            mod0.summary.predictions[['prediction']].collect())

plt.figure()
plt.scatter(data_raw[['passengers']].collect(),
            data_raw[['crew']].collect())

plt.figure()
plt.scatter(data_raw[['cabins']].collect(),
            data_raw[['crew']].collect())


#%%
#%%
eval_test = mod0.evaluate(data_test)
eval_test.r2
eval_test.rootMeanSquaredError

eval_train = mod0.evaluate(data_train)
eval_train.r2
eval_train.rootMeanSquaredError

eval_train.predictions.show()

#%%




#%%



#%%

