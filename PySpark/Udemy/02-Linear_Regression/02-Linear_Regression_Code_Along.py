#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Linear Regression
subtitle: E-commerce Example
version: 1.0
type: course
keywords: [linear regression, big data, PySpark]
description: |
remarks:
todo:
sources:
    - title: Spark and Python for Big Data with PySpark
      chapter: Linear Regression
      section: Lecture 37 - Code along example
      pages:
      link: https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/learn/lecture/6688262#overview
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
    name: 02-Linear_Regression_Code_Along.py
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
spark = SparkSession.builder.appName("linreg2").getOrCreate()

from pyspark.ml.regression import LinearRegression

#%%
data_raw = spark.read.csv("Ecommerce_Customers.csv", inferSchema=True, header=True)
data_raw.printSchema()
data_raw.count()  # 500
data_raw.head().asDict()

#%%
# from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

data_raw.columns

assembler = VectorAssembler(
                inputCols=["Avg Session Length", "Time on App",
                           "Time on Website", "Length of Membership"],
                outputCol="features")

output = assembler.transform(data_raw)
output.head().asDict()

#%%
data_all = output.select(output['Yearly Amount Spent'].alias('yas'), 'features')
data_all.head().asDict()

data_train, data_test = data_all.randomSplit([.7, .3])
data_train.describe().show()
data_test.describe().show()

#%%
lr = LinearRegression(featuresCol="features", labelCol="yas")

mod = lr.fit(data_train)
mod.coefficients
mod.intercept

#%% to get measures of gof one must first evaluate model!
mod.r2  #!!! AttributeError: 'LinearRegressionModel' object has no attribute 'r2'

# on test data
eval_test = mod.evaluate(data_test)
eval_test.r2   # 0.9836994539855342
eval_test.rootMeanSquaredError  # 9.386096376602243

# on train data
eval_train = mod.evaluate(data_train)
eval_train.r2   # 0.9844092656344741    # obviously better but only a little
eval_train.rootMeanSquaredError  # 10.177554035271772

#%%
import matplotlib.pyplot as plt
y = data_test[['yas']].collect()
y_hat = eval_test.predictions[['prediction']].collect()
plt.scatter(y, y_hat)
plt.plot([300, 700], [300, 700])


#%%



#%%




#%%
