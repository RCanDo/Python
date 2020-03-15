#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Using Apache Arrow
version: 1.0
type: usage example
keywords: [PyArrow, Pandas, PySpark, Apache]
description: |
remarks:
    - install PyArrow `pip install pyarrow` (?)
todo:
sources:
    - title: Optimizing Conversion between Spark and Pandas DataFrames using 
         Apache PyArrow
      link: https://blog.clairvoyantsoft.com/optimizing-conversion-between-spark-and-pandas-dataframes-using-apache-pyarrow-9d439cbf2010
      date: 2019-08-20
      authors:
          - fullname: Maneesh Kumar
      usage: copy
    - link: https://arrow.apache.org/
    - title: Python library for Apache Arrow
      link: https://github.com/apache/arrow/tree/master/python
    - title: PySpark Usage Guide for Pandas with Apache Arrow
      link: https://spark.apache.org/docs/latest/sql-pyspark-pandas-with-arrow.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: PyArrow.py
    path: ~/Works/Python/PySpark/other/
    date: 2020-03-01
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""

#%% 
cd ~/Works/Python/PySpark/other/

#%%
import pandas as pd
import numpy as np
from pyspark.sql import SparkSession

spark = SparkSession.builder.master('local').appName('pyarrow').getOrCreate()

#%%
pdf1 = pd.DataFrame(np.random.rand(int(1e5), 3))

#%%
%timeit  spark.createDataFrame(pdf1)
# 6.79 s ± 184 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

#%%
df1 = spark.createDataFrame(["10", "11", "12"], "string").toDF("age")
df1.show()

%timeit df1.toPandas()

#%%
spark.conf.set("spark.sql.execution.arrow.enabled", "true")

#%%
pdf2 = pd.DataFrame(np.random.rand(int(1e5), 3))

%timeit  spark.createDataFrame(pdf2)
# 6.63 s ± 57.4 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) 

#%%


#%%

