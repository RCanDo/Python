#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Logistic Regression
subtitle: Consulting Project - Customer Churn
version: 1.0
type: course
keywords: [pipelines, logistic regression, big data, PySpark]
description: |
remarks:
todo:
sources:
    - title: Spark and Python for Big Data with PySpark
      chapter: Logistic Regression
      section: Lecture 43 - Logistic Regression Consulting Project
      link: https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/learn/lecture/6688270#overview
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
    name: 03-Logistic_Regression_Consulting_Project.py
    path: ~/Works/Python/PySpark/Udemy/03-Logistic_Regression/
    date: 2020-01-14
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

spark = SparkSession.builder.appName('customer_churn').getOrCreate()

#%%
data_raw = spark.read.csv("customer_churn.csv", inferSchema=True, header=True)
data_raw.head(3)
data_raw.printSchema()
data_raw.count()   # 900
data_raw.describe().show()

data_raw.select('Location').show(9, False)

#%%
#%%
from pyspark.sql.functions import regexp_extract, regexp_replace

# check
data_raw.select(regexp_extract('Location', r'(, )(\w\w)', 2).alias('State')) \
    .select(regexp_replace('State', r'^$', 'none').alias('State')).show()

#%% apply
def extract_state(df):
    data = df.withColumn('State', 
                    regexp_replace(
                        regexp_extract('Location', r'(, )(\w\w)', 2),
                        r'^$', 'none'
                    ))
    return data

#%%
data_r = extract_state(data_raw)
data_r.printSchema()
data_r.select('State').show()
    
data_r.groupBy('State').count().orderBy('count').show(100, False)

#%%
#%% the problem is - this should be some transormation from pyspark.ml.feature
# but there is only  RegexTokenizer  which cannot do what is in the function.
# we need to create our own custom Transformer - it is nothing more then
# function extract_state() above enveloped with proper class:

from pyspark.ml import Transformer 
from pyspark.sql.functions import regexp_extract, regexp_replace  # to remember

class ExtractState(Transformer):
    
    def transform(self, df):
        data = df.withColumn('State', 
                        regexp_replace(
                            regexp_extract('Location', r'(, )(\w\w)', 2),
                            r'^$', 'none'
                        ))
        return data
    
extract_State = ExtractState()  # to be used in Pipeline
        
#%%
data = data_raw.select('Age', 'Total_Purchase', 'Account_Manager',
                       'Years', 'Num_Sites', 
                       'Location', 'Churn')

#%%
data.show()
data.count()

data.na.df.show()    #??
data.na.df.count()    #??
data.na.drop()
data.count()  # 900
# no NAs

data.describe().show()
data.printSchema()

#%% plots !!!

#%%
data_train, data_test = data.randomSplit([.7, .3])
n_train = data_train.count()  # 659
n_test = data_test.count()    # 241

#%%
from pyspark.ml.feature import VectorAssembler, VectorIndexer, \
                               OneHotEncoder, StringIndexer
                               
index_State = StringIndexer(inputCol='State', outputCol='StateIdx')
encode_State = OneHotEncoder(inputCol='StateIdx', outputCol='StateOH')

#%%
assembler = VectorAssembler(inputCols=['Age', 'Total_Purchase', 'Account_Manager',
                                       'Years', 'Num_Sites', 'StateOH'],
                            outputCol='features')

#%%
from pyspark.ml.classification import LogisticRegression

logreg = LogisticRegression(featuresCol='features', labelCol='Churn')

#%%
from pyspark.ml import Pipeline

pipeline = Pipeline(stages=[extract_State, index_State, encode_State, assembler, logreg])
dir(pipeline)
pipeline.stages
list(pipeline.stages)   #! TypeError: 'Param' object is not iterable
dir(pipeline.stages)
pipeline.getStages()
pipeline.params

#%%
model_fit = pipeline.fit(data_train)
type(model_fit)    # pyspark.ml.pipeline.PipelineModel
model_fit.summary  #! AttributeError: 'PipelineModel' object has no attribute 'summary'
dir(model_fit)

#!!! PRETTY SHIT !!! 
# What can I do with such a "Model"???
# No information about its quality, which variables are significant, etc...

#%%
# The only solution is to NOT include logreg into pipeline...
# This way we test in the next file, here let's continue.

#%%
pred_test = model_fit.transform(data_test)
pred_test.select('State').show(99)

pred_test.printSchema()
pred_test.select('Churn', 'prediction', 'probability', 'rawPrediction').show(99, False)

#%%
from pyspark.ml.evaluation import BinaryClassificationEvaluator

evaluation = BinaryClassificationEvaluator(rawPredictionCol='prediction',
                                           labelCol='Churn')

evaluation.evaluate(pred_test)  # 0.7057787174066243  = AUC

dir(evaluation)

#??? How to find model parameters significance ???
# and other measures of model quality ???

#%% 
#%% new data
data_new = spark.read.csv('new_customers.csv', inferSchema=True, header=True)
pred_new = model_fit.transform(data_new)  # ? , params={'handleInvalid': 'keep'}) # doesn't work

pred_new.show()  #! Unseen label: Yo.  To handle unseen labels, set Param handleInvalid to keep.
pred_new.select('State').show()
pred_new.select('prediction').show()  #! Unseen label: Yo.  To handle unseen labels, set Param handleInvalid to keep.
pred_new.printSchema()
pred_new.count()

#%% fast solution - get rid of this record
# but we should do it better!!! replace invalid value with 'none'

data_new = data_new.filter(data_new.Names != 'Michele Wright')
pred_new = model_fit.transform(data_new)  # ? , params={'handleInvalid': 'keep'}) # doesn't work

pred_new.show()
pred_new.select('Names', 'prediction').show()

#%%
