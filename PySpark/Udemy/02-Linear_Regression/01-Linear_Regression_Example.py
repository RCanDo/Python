#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Linear Regression
subtitle: Example
version: 1.0
type: course
keywords: [linear regression, big data, PySpark]
description: |
remarks:
todo:
sources:
    - title: Spark and Python for Big Data with PySpark
      chapter: Linear Regression
      section: Lecture 35 - Documentation Example
      pages:
      link: https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/learn/lecture/6986092#overview
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
    name: 01-Linear_Regression_Example.py
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
spark = SparkSession.builder.master("local").appName("linreg").getOrCreate()

data = spark.read.format("libsvm").load("sample_linear_regression_data.txt")
data.show()
data.count()  # 501
data[['features']].head()

#%%
from pyspark.ml.regression import LinearRegression

lr = LinearRegression(featuresCol='features',
                      labelCol='label',
                      predictionCol='prediction')
mod0 = lr.fit(data)

#%%
mod0.coefficients
mod0.intercept
mod0.summary.residuals.describe().show()
mod0.summary.rootMeanSquaredError
mod0.summary.r2

import matplotlib.pyplot as plt
plt.scatter(range(501), mod0.summary.residuals.collect())

#%%
"""
but we have no data to evaluate model;
we should have splitted data into training and test part
"""
data_train, data_test = data.randomSplit([.7, .3])
n_train = data_train.count() # 378
n_test = data_test.count()  # 123

mod = lr.fit(data_train)

#%%
mod.coefficients
mod.intercept
mod.summary.residuals.describe().show()
mod.summary.rootMeanSquaredError
mod.summary.r2

plt.scatter(range(n_train), mod.summary.residuals.collect())  # !!! ???

#%%
eval_test = mod.evaluate(data_test)
eval_test.rootMeanSquaredError
eval_test.r2
plt.scatter(range(n_test), eval_test.residuals.collect())

#%% predictions from the model
eval_test.predictions.show()

y = eval_test.predictions[['label']].collect()
x = eval_test.predictions[['features']].collect()
y_hat = eval_test.predictions[['prediction']].collect()

# compare predictions (y^) with real labels (y)
plt.scatter(y, y_hat)
# pretty mess...

#%% the other way

y0 = data_test.select('label').collect()       # .select('.') == [['.']]
x0 = data_test.select('features').collect()

# check if these are the same vectors
plt.scatter(x, x0)
plt.scatter(y, y0)
# OK they are equal

pred_test = mod.transform(data_test[['features']])  #!!!
pred_test  # data frame ['features', 'prediction']
y_hat0 = pred_test[['prediction']].collect()
plt.scatter(y_hat, y_hat0)
# OK the same

# once again
plt.scatter(y0, y_hat0)  # mess...

#%%


#%%


#%%
