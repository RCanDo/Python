# -*- coding: utf-8 -*-
"""
title: Mastering pandas
subtitle: based on "Mastering pandas.pdf" (book) by Femi Anthony
author: kasprark
date: Tue Jan 16 14:08:12 2018

summary01. DataFrames
=====================
"""
## •

%reset

pwd
cd c:/PROJECTS/Python/tuts/Mastering pandas/
ls

import importlib ## may come in handy

import pandas as pd

# importlib.reload(pd)

import numpy as np

#%%
"""
DataFrame Creation
------------------
"""

### pd.Series

ss1 =  pd.Series([346.15, 0.59, 459],
                 index=['Closing price', 'EPS', 'Shares Outstanding(M)'])
ss1

## number of entries must agree
pd.Series([346.15, 0.59, 459], index=['Closing price', 'EPS'])  ## ValueError:
pd.Series([346.15, 0.59], index=['Closing price', 'EPS', 'Shares Outstanding(M)'])  ## ValueError:

#%%
"""
Creating DataFrames from dictionary of pd.Series
where each entry of dict. is a separate column with its own type.
"""

stockSummaries={'AMZN': pd.Series([346.15,0.59,459,0.52,589.8,158.88],
                                  index=['Closing price','EPS','Shares Outstanding(M)',
                                         'Beta', 'P/E','Market Cap(B)']),
                'GOOG': pd.Series([1133.43,36.05,335.83,0.87,31.44,380.64],
                                  index=['Closing price','EPS','Shares Outstanding(M)',
                                         'Beta','P/E','Market Cap(B)']),
                  'FB': pd.Series([61.48,0.59,2450,104.93,150.92],
                                  index=['Closing price','EPS','Shares Outstanding(M)',
                                         'P/E', 'Market Cap(B)']),
                'YHOO': pd.Series([34.90,1.27,1010,27.48,0.66,35.36],
                                  index=['Closing price','EPS','Shares Outstanding(M)',
                                         'P/E','Beta', 'Market Cap(B)']),
                'TWTR': pd.Series([65.25,-0.3,555.2,36.23],
                                  index=['Closing price','EPS','Shares Outstanding(M)',
                                         'Market Cap(B)']),
                'AAPL': pd.Series([501.53,40.32,892.45,12.44,447.59,0.84],
                                  index=['Closing price','EPS','Shares Outstanding(M)','P/E',
                                         'Market Cap(B)','Beta'])}

stockSummaries
type(stockSummaries)
stockSummaries.keys()
list(stockSummaries.keys())[1:3]


stockDF = pd.DataFrame(stockSummaries)
stockDF

## setting row-index (selection and order of items)
pd.DataFrame(stockSummaries, index = ['Closing price','EPS', 'Shares Outstanding(M)', 'P/E'
                                      ,'Market Cap(B)','Beta'])

pd.DataFrame(stockSummaries, index = ['Closing price','EPS', 'Shares Outstanding(M)', 'P/E']) 

## setting columns (selection and order)
pd.DataFrame(stockSummaries, index=['Closing price','EPS','Shares Outstanding(M)','P/E'
                                    ,'Market Cap(B)','Beta'],
             columns=['FB','TWTR','SCNW'])

## 
stockDF.columns
stockDF.index

#%%
"""
from dictionary of ndarrays/lists
"""

algos={'search'  : ['DFS','BFS','Binary Search','Linear','ShortestPath (Djikstra)'],
       'sorting' : ['Quicksort','Mergesort', 'Heapsort','Bubble Sort', 'Insertion Sort'],
       'machine learning': ['RandomForest','K Nearest Neighbor','Logistic Regression',
                            'K-Means Clustering','Linear Regression']}
       
algos       

algoDF = pd.DataFrame(algos)
algoDF
algoDF.index
algoDF.columns

pd.DataFrame(algos, columns = ["sorting","search","machine learning"])
pd.DataFrame(algos, index = ["alg0","alg1","alg2","alg3","alg4"])
pd.DataFrame(algos, index = ["alg{:2d}".format(i) for i in range(len(algos['search']))])

#%%
"""
Using array
"""

aa1 = np.array([ [1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [10, 11, 12] ] )
aa1       

pd.DataFrame(aa1)
pd.DataFrame(aa1, columns=['a', 'b', 'c'])
pd.DataFrame(aa1, columns=['x', 'y', 'z'], index=['a', 'b', 'c', 'd'])
  pd.DataFrame(aa1, index=['x', 'y', 'z'], columns=['a', 'b', 'c', 'd'])   ## ERROR
pd.DataFrame(aa1.T, index=['x', 'y', 'z'], columns=['a', 'b', 'c', 'd'])   


#%%
"""
Using tuple ???
"""

tpl = ( [1,2], [3.4], [5,6] )
tpl
pd.DataFrame(tpl)    ## ValueError: DataFrame constructor not properly called!

### list of lists
tpl = [ [1,2], [3.4], [5,6] ]
tpl
pd.DataFrame(tpl)

### list of lists
tpl2 = [ [1,'a'], [3.4,'b'], [5,'c'] ]
tpl2
pd.DataFrame(tpl2)
pd.DataFrame(np.transpose(tpl2))


### list of tuples
tpl3 = [ (1,2), (3.4,), (5,6) ]
tpl3
pd.DataFrame(tpl3)


#%%
"""
Using a structured array  ???
"""
aa1 = np.array([('e', 2.71828 ),
                ('ln', 0 ),
                ('cos', 1 )
               ], dtype=[ ('str','a15'), ('val','f4') ] )
aa1

pd.DataFrame(aa1)

#%%

memberData = np.zeros( (4,),
                      dtype=[('Name','a15'),
                             ('Age','i4'),
                             ('Weight','f4')])
memberData
type(memberData)

memberData[:] = [('Sanjeev', 37 ,162.4),
                 ('Yingluck', 45 ,137.8),
                 ('Emeka', 28, 153.2),
                 ('Amy', 67, 101.3)]
memberData

pd.DataFrame(memberData)
memberDF = pd.DataFrame(memberData, index=['a','b','c','d'])
memberDF

#%%
"""
Using Series
"""
currSeries = pd.Series( ["yuan","euro","yen","peso","naira","pound","dollar"] , 
                        index = ["China","Germany","Japan","Mexico","Nigeria","UK","US"]
                       )
currSeries

currSeries.index
currSeries.values

pd.DataFrame(currSeries)


#%%
"""
DataFrame Operations
--------------------
"""

### Selection
algoDF['search']
algoDF[['search','sorting']]
algoDF[['search','sorting']][1:4]

algoDF[:]
algoDF[1:3]
algoDF[1:3]['search']
algoDF[1:3][['search','sorting']]
algoDF[1:3][['sorting']]

memberDF[:][1:3]
memberDF[:][['b','c']]   ## KeyError: "['b' 'c'] not in index"

## more on this in Indexing

### Assignment
memberDF['Height'] = 60; memberDF
memberDF['Height'][2]
memberDF['Height'][2:4]
memberDF['Height'][2:4] = 70  ## SettingWithCopyWarning:  A value is trying to be set on a copy of a slice from a DataFrame
memberDF

### Deletion
del memberDF['Height']; memberDF

memberDF['BloodType'] = '0'; memberDF
bloodType = memberDF.pop('BloodType'); bloodType
memberDF

### Insertion
memberDF.insert(2,'isSenior',memberDF['Age']>60)
memberDF 

memberDF.insert(3,'isLight',memberDF['Weight']<150); 
memberDF

#%%
### Alignment
ore1DF = pd.DataFrame( np.array([[20,35,25,20],
                                [11,28,32,29]]),
                        columns=['iron','magnesium','copper','silver']
                     )
ore1DF

ore2DF = pd.DataFrame( np.array([[14,34,26,26],
                                [33,19,25,23]]),
                        columns=['iron','magnesium','gold','silver']
                     )
ore2DF

ore1DF + ore2DF

[25 for k in range(4)]
ore1DF + pd.Series([25 for k in range(4)], index=['iron','magnesium','copper','silver'])
ore1DF + pd.Series([25 for k in range(4)], index=ore1DF.columns)

#%%
ore1DF ** 2
ore1DF.T
ore1DF + ore1DF.T   ## ???

pd.DataFrame(np.array(ore1DF)[:,1:2] + np.array(ore1DF.T)[1,:])

#%%
"""
More on indexing on DataFrames in separate chapter/file
C:\PROJECTS\Python\tuts\Mastering Pandas\MasteringPandas-04-Indexing.ipynb  
or
C:\PROJECTS\Python\tuts\Mastering Pandas\MasteringPandas-04-Indexing.py
"""