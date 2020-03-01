#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Logistic Regression
subtitle: Consulting Project - Customer Churn
version: 2.0
type: course
keywords: [pipelines, logistic regression, big data, PySpark]
description: |
    In this version we do not enclose logreg model into a pipeline
    as the final PipelineModel does not allow to see any summary of the model
    - hence it's hard to asses model quality or variable significance.
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
data_raw.toPandas()
data_raw.toJSON()

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

#%% only presentation
data_r = extract_state(data_raw)
data_r.printSchema()
data_r.select('State').show()
    
data_r.groupBy('State').count().orderBy('count').show(100, False)

#%%
#%% the problem is - this should be some transformation from pyspark.ml.feature
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
n_train = data_train.count()  # 629
n_test = data_test.count()    # 271

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
from pyspark.ml import Pipeline
pipeline = Pipeline(stages=[extract_State, index_State, encode_State, assembler])

type(pipeline)
# A simple pipeline, which acts as an Estimator. 
# A Pipeline consists of a sequence of stages, 
# each of which is either an Estimator or a Transformer. ...
# Estimator has .fit() which returns Model which is Transformer.
# Transformer has .transform()

pipeline_fit = pipeline.fit(data_train)
# this is peculiar but notice that pipeline is an Estimator and has only .fit()
# method and do not have .transform() method.
# In this case there is nothing to fit... but works!
type(pipeline_fit)   # pyspark.ml.pipeline.PipelineModel

data_train_p = pipeline_fit.transform(data_train)
data_train_p.printSchema()
data_train_p.select('State', 'StateIdx', 'StateOH').show()

data_test_p = pipeline_fit.transform(data_test)
data_test_p.printSchema()
data_test_p.select('State', 'StateOH').show()

#%%
from pyspark.ml.classification import LogisticRegression
logreg = LogisticRegression(featuresCol='features', labelCol='Churn')
type(logreg)

#%%
model_fit = logreg.fit(data_train_p.select('features', 'Churn'))
model_fit.summary.accuracy     # 0.9240710823909531
model_fit.summary.predictions.show()

model_fit.summary.predictions.describe().show()

#%%
model_eval = model_fit.evaluate(data_test_p.select('features', 'Churn'))
model_eval.predictions.show()

#%%
from pyspark.ml.evaluation import BinaryClassificationEvaluator

evaluation = BinaryClassificationEvaluator(rawPredictionCol='prediction',
                                           labelCol='Churn')

evaluation.evaluate(model_eval.predictions)  # 0.6425342130987293 = AUC

#%% 
#%% new data
data_new = spark.read.csv('new_customers.csv', inferSchema=True, header=True)
data_new.count()   # 6
data_new.show()

data_new_p = pipeline_fit.transform(data_new)
data_new_p.printSchema()
data_new_p.show()  #! Unseen label: Yo.  To handle unseen labels, set Param handleInvalid to keep.

#%% fast solution - get rid of this record
# but we should do it better!!! replace invalid value with 'none'

data_new = data_new.filter(data_new.Names != 'Michele Wright')
data_new_p = pipeline_fit.transform(data_new)  # ? , params={'handleInvalid': 'keep'}) # doesn't work
data_new_p.show()

pred_new = model_fit.transform(data_new_p)

pred_new.show()
pred_new.select('Names', 'Company', 'prediction').show()

#%%


