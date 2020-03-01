#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Decision Trees And Random Forest
subtitle: Consulting Project - 
version: 1.0
type: course
keywords: [Gradient Boosted Trees, Decision Trees, Random Forest, Big Data, PySpark]
description: |
remarks:
todo:
sources:
    - title: Spark and Python for Big Data with PySpark
      chapter: Decision Trees And Random Forest
      section: Lecture 48 - Tree Methods Consulting Project
      link: https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/learn/lecture/7023948#announcements
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
    name: 03-Tree_Methods_Consulting_Project.py
    path: ~/Works/Python/PySpark/Udemy/04-Tree_Methods/
    date: 2020-02-29
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
spark = SparkSession.builder.master('local').appName('trees_con_proj').getOrCreate()

#%%
data_raw = spark.read.format('csv').load('dog_food.csv', iferSchema=True, header=True)
data_raw.count()   # 490

data_raw.printSchema()
data_raw.show()


#%% digression about types in Spark
from pyspark.sql.functions import col   # convienient reference to column
data_raw.withColumn('A', col('A').cast('float')).printSchema()
data_raw.withColumn('A', col('A').cast('int')).printSchema()

#%%
from pyspark.sql.types import FloatType, IntegerType
data_raw.withColumn('A', col('A').cast(FloatType())).printSchema()
data_raw.withColumn('A', col('A').cast(IntegerType())).printSchema()

#%%
from pyspark.sql import types 

for t in ['BinaryType', 'BooleanType', 'ByteType', 'DateType', 
          'DecimalType', 'DoubleType', 'FloatType', 'IntegerType', 
           'LongType', 'ShortType', 'StringType', 'TimestampType']:
    print(f"{t}: {getattr(types, t)().simpleString()}")
    
#%%
from pyspark.ml import Transformer

class ToFloats(Transformer):
    
    def __init__(self, *args):
        super().__init__()
        self.args = args
        
    def transform(self, df):
        for col in self.args:
            df = df.withColumn(col, df[col].cast("float"))
        return df
    
to_floats = ToFloats(*list('ABCD'))        

#%%
#%%
from pyspark.ml.feature import StringIndexer

indexer_Spoiled = StringIndexer(inputCol='Spoiled', outputCol='SpoiledIdx')

#%%
from pyspark.ml.feature import VectorAssembler

assembler = VectorAssembler(outputCol='features', inputCols=list('ABCD')) 

#%% 

class ColumnsSelector(Transformer):
    
    def __init__(self, *args):
        super().__init__()
        self.args = args
        
    def transform(self, df):
        return df[[*self.args]]
    
selector = ColumnsSelector('SpoiledIdx', 'features')

#%%
from pyspark.ml import Pipeline
pipeline = Pipeline(stages=[to_floats, indexer_Spoiled, assembler, selector])

data = pipeline.fit(data_raw).transform(data_raw)

data.show()

data_train, data_test = data.randomSplit([.7, .3])
print(f'{data_train.count()}, {data_test.count()}')   # 322, 168

#%%
from pyspark.ml.classification import DecisionTreeClassifier, \
                                      RandomForestClassifier, \
                                      GBTClassifier


est_dt = DecisionTreeClassifier(featuresCol='features', labelCol='SpoiledIdx')
est_rf = RandomForestClassifier(featuresCol='features', labelCol='SpoiledIdx')
est_gb = GBTClassifier(featuresCol='features', labelCol='SpoiledIdx')

#%%
model_dt = est_dt.fit(data_train)
model_rf = est_rf.fit(data_train)
model_gb = est_gb.fit(data_train)
                                 
#%%
dir(model_dt)
model_dt.featureImportances
model_rf.featureImportances
model_gb.featureImportances

#%%                                  
vv = model_gb.featureImportances
dir(vv)
vv.values

#%%
import matplotlib.pyplot as plt
      
plt.figure()
for mod in [model_dt, model_rf, model_gb]:
    vv = mod.featureImportances.values
    plt.plot(vv)
                             
#%%

#%%