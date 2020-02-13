# -*- coding: utf-8 -*-
"""
title: Mastering pandas
subtitle: based on "Mastering pandas.pdf" (book) by Femi Anthony
author: kasprark
date: Fri Dec 29 08:49:41 2017

10. R and pandas compared
=========================
(p. 257)
"""
## •

%reset

pwd
cd "C:\Users\akasprzy\OneDrive - HERE Global B.V-\arek\ROBOCZY\Python\help\Mastering Pandas"
ls

import importlib ## may come in handy
import pandas as pd
# importlib.reload(pd)
import numpy as np

#%%
'''
R data types
------------
R has five primitive or atomic types:

• Character
• Numeric
• Integer
• Complex
• Logical/Boolean

It also has the following, more complex, container types:
• Vector: This is similar to `numpy.array`. It can only contain objects of the same type.
• List: It is a heterogeneous container. Its equivalent in pandas would be a `series`.
• DataFrame: It is a heterogeneous 2D container, equivalent to a pandas `DataFrame`.
• Matrix: It is a homogeneous 2D version of a vector. It is similar to a `numpy.matrix`.

For this chapter, we will focus on `list` and `DataFrame`,
which have pandas equivalents as `series` and `DataFrame`.

For more information on R data types, refer to the following document at:
    http://www.statmethods.net/input/datatypes.html.
For NumPy data types, refer to the following document at:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html
    and
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html.
'''

#%%
'''
R lists --- pandas.series
-------
> list(23,'donkey',5.6,1+4i,TRUE)

Here is its `series` equivalent in pandas with the creation of a [python's] `list`
and the creation of a `series` from it:
'''

ss = pd.Series( [23, 'donkey', [5.6, 1+4j], True] )
ss
type(ss)
ss[0]
ss[2]
ss[2][1]
len(ss)    ## 4
ss[3]
ss.shape

ss.  ## huge number of methods ...

#%% contrary to python's list pandas.Series can be named:
ss.index = ['a','b','c','d']
ss
ss[0]
ss['a']
ss[['a','b']]
ss[:2]

## or on the fly
ss = pd.Series( [23, 'donkey', [5.6, 1+4j], True] , index = ['a','b','c','d'])
ss

ss.append( pd.Series( ['qq', 1, False] ) )  ## names and numbers mixed

## removing names == resetting them to numeric
ss.index = range(len(ss))
ss


#%%
ss.append()

ss.append( pd.Series( ['qq', 1, False] ) )
ss          ## nothing changed...

ssap = ss.append( pd.Series( ['qq', 1, False] ) )
ssap
len(ssap)
ssap[0]    ## indices repeat
ssap[2]

ssap = ss.append( pd.Series( [ ['qq', 1, False] , 'the lonely last' ] ) )
ssap
len(ssap)
ssap[0]    ## indices repeat
ssap[2]

#%%
s1 = pd.Series([1, 2, 3])
s1
s2 = pd.Series([4, 5, 6])
s2
s3 = pd.Series([4, 5, 6], index=[3,4,5])
s3

s1.append(s2)
#    0    1
#    1    2
#    2    3
#    0    4
#    1    5
#    2    6
#    dtype: int64

s1.append(s3)
#    0    1
#    1    2
#    2    3
#    3    4
#    4    5
#    5    6
#    dtype: int64
#    With ignore_index set to True:
s11 = s1.append(s3)
s11

s1.append(s2, ignore_index=True)
#    0    1
#    1    2
#    2    3
#    3    4
#    4    5
#    5    6
#    dtype: int64
s12 = s1.append(s2, ignore_index=True)
s12

s1.append(s2, verify_integrity=True)
#    Traceback (most recent call last):
#    ...
#    ValueError: Indexes have overlapping values: [0, 1, 2]


#%%
'''
R data.frames --- pandas DataFrames
-----------------------------------
> stocks.df <- data.frame( Symbol    = c('GOOG', 'AMZN', 'FB', 'AAPL', 'TWTR', 'NFLX', 'LINKD'),
                           Price     = c(518.7, 307.82, 74.9, 109.7, 37.1, 334.48, 219.9),
                           MarketCap = c(352.8, 142.29, 216.98, 643.55, 23.54, 20.15, 27.31)
                         )

Pandas DataFrame is a wrapper over [python's] `dictionary` having `lists` (all of the same length) as items:
'''
stocks_df = pd.DataFrame( { 'Symbol'    : ['GOOG', 'AMZN', 'FB', 'AAPL', 'TWTR', 'NFLX', 'LINKD'],
                            'Price'     : [518.7, 307.82, 74.9, 109.7, 37.1, 334.48, 219.9],
                            'MarketCap' : [352.8, 142.29, 216.98, 643.55, 23.54, 20.15, 27.31]
                          } )

stocks_df
len(stocks_df)  ## 7 -- a number of rows!!!
stocks_df.shape ## (7, 3)

type(stocks_df)
type(stocks_df['Symbol'])    ##!!!  pandas.core.series.Series  !!!

stocks_df[:]    ## OK!
stocks_df[1,:]  ## TypeError: unhashable type: 'slice'
stocks_df[:,1]  ## TypeError: unhashable type: 'slice'

## so, how to slice and select ???

#%%
'''
Slicing and selection
---------------------
'''

#%%
'''
NumPy arrays
------------
Let's now see NumPy array creation and selection:
'''
import numpy as np

a = np.array(range(2,6))
b = np.array(range(6,10))
c = np.array(range(10,14))
a
b
c
type(a)  ## numpy.ndarray

arr = np.column_stack([a, b, c])
arr
type(arr)  ## numpy.ndarray

'''
NumPy array is a list of lists (all of the same length);
these lists are considered as ROWs !!! i.e. they are _stacked_ one over the other,
although we've used  np.column_stack(a, b, c)  where lists  a, b, c  are "stacked" one _aside_ the other
(that's NOT a good name for function as "stack" has the first meaning rather!).
'''

## one index means rows for np.arrays
arr[0]
arr[0:2]

## two indices means [row,column]
arr[0,]     ## OK !
arr[,1]     ## SyntaxError: invalid syntax
arr[0,:]
arr[:,1]

arr[0:1,]   ## in Python n:m means n,...,m-1   !!!
arr[0:2,]

### transposition is a method
arr.T
### although there is a function
np.transpose(arr)

arr.T[0]
arr.T[1:3,1:4]

#%%
'''
R lists and pandas series compared
----------------------------------

If you wish to use analog of R's named list you need to create a named Series by calling pd.Series()
on dictionary rather then list.
'''

ss2 = pd.Series({ 'weekdays' : list(range(1,8)) , 'mth' : 'january' , 'year' : 2017  , 'aaa' : ['qq',11]})
ss2
type(ss2)

## Notice the order!!! It is ALPHABETICAL !!!

#%%
'''
### Specifying Series element name in pandas

Indexing named Series is possible in two ways:
'''

## via names
ss2['mth']
ss2['weekdays']

## via integer indices
ss2[0]
ss2[1]
ss2[1][2]
ss2['weekdays'][2]

#%%
## notice that
ss2[1]
ss2[[1]]

type(ss2[1])    ## content of the Series at position 1
len(ss2[1])
type(ss2[[1]])  ## subseries (of length 1) of the Series
len(ss2[[1]])
ss2[[1]]

## Notice that
ss2[['mth','year']]     ## OK
ss2[[1,3]]
ss2[[1:3]]              ## SyntaxError: invalid syntax
ss2[1:3]                ## OK
ss2[(1,3)]              ## KeyError: (0, 2)
ss2[1:4:2]              ## OK

ss2[k for k in range(4)]  ## SyntaxError: invalid syntax
ss2[[k for k in range(4)]] 

'''
    So this is opposite to R where [] is a sublist and [[]] is its content !!!

E.g.
> ll[1]         ## sublist of ll consisting of only first element;
                ## in Python : ll[[0]]
> type(ll[1])   ## "list"
> ll[1:3]       ## sublist of ll consisting of elements 1,2,3;
                ## in Python : ll[0,1,2]
> ll[c(1,2,4)]  ## sublist of ll consisting of elements 1,2,4;
                ## in Python : ll[[0,1,3]]
> ll[[1]]       ## the content of the first element of ll
                ## in Python : ll[0]
> ll[[1:2]]     ## ERROR: cannot return contents of two elements symultaniously
                ## in Python : ll[0:2]  will work but return sublist!
'''


#%%
'''
DataFrames
----------
'''

#%% !!!
### You cannot use integer indices of columns for DataFrame
stocks_df[1]        ## KeyError: 1
stocks_df[,1]       ## SyntaxError: invalid syntax
stocks_df[:,1]      ## TypeError: unhashable type: 'slice'

stocks_df[1:3]      ## OK! but works on rows
stocks_df[0:1]
stocks_df[0:2]

#%%
### Only names of columns are allowed

stocks_df['Price']
type(stocks_df['Price'])      ## pandas.core.series.Series
stocks_df[['Price']]
type(stocks_df[['Price']])    ## pandas.core.frame.DataFrame
stocks_df[['Price','Symbol']]
stocks_df[['Symbol','Price']]

stocks_df['Symbol','Price']   ## KeyError: ('Symbol', 'Price')

#%%
### and if you need to select columns and rows then you must use .loc[] method

stocks_df[:,['Symbol','Price']]     ## TypeError: unhashable type: 'slice'
stocks_df.loc[:,['Symbol','Price']]     #!#! use of .loc[]  method ...
stocks_df.loc[1:3,['Symbol','Price']]

stocks_df.loc[::-1,['Symbol','Price']]

stocks_df.loc[::-1,]
stocks_df.loc[::-1,:]
stocks_df.loc[::-1,1:3]  ## TypeError: cannot do slice indexing on <class 'pandas.core.indexes.base.Index'>
stocks_df.loc[::-1,::-1] ## That's OK !!!

stocks_df.loc[::-1,['Price','Symbol']]
stocks_df.loc[::-1,][['Price','Symbol']]
stocks_df.loc[::-1][['Price','Symbol']]
stocks_df.loc[::-1]
stocks_df.loc[1:3]
stocks_df.loc[1]
type(stocks_df.loc[1])      ## pandas.core.series.Series

#%%
'''
Arithmetic operations on columns
--------------------------------
'''

df = pd.DataFrame( {  'x' : np.random.normal(0, 1, size=7)
                    , 'y' : np.random.normal(0, 1, size=7)
                   } )

df
type(df)
df.x
type(df.x)
df['x']
type(df['x'])       ## pandas.core.series.Series
type(np.random.normal(0, 1, size=7) )   ## numpy.ndarray

df[['x']]
type(df[['x']])     ## pandas.core.frame.DataFrame

## Way 1.
diffxy = df.x - df.y
diffxy
type(diffxy)  ## pandas.core.series.Series

## Way 2.
diffxy = df.eval('x-y')
diffxy
type(diffxy)

#%%
'''
Aggregation and GroupBy
-----------------------
'''

goals_df = pd.read_csv('champ_league_stats_semifinalists.csv',sep=";")
goals_df

type(goals_df)
goals_df.shape

goals_df['GoalsPerGame'] = goals_df['Goals']/goals_df['GamesPlayed']
goals_df

goals_df['GoalsPerGame'] = goals_df.eval('Goals/GamesPlayed')
goals_df

## .groupby()
grouped = goals_df.groupby('Club')
grouped         ## data invisible, just an object...
type(grouped)   ## pandas.core.groupby.DataFrameGroupBy

## .aggregate()
grpd1 = grouped['GoalsPerGame'].aggregate(np.max)
grpd1
type(grpd1)  ## pandas.core.series.Series

grpd2 = grouped[['Goals','GoalsPerGame']].aggregate(np.max)
grpd2
type(grpd2)  ## pandas.core.frame.DataFrame

grouped[['Goals','GoalsPerGame']].aggregate(np.mean)
grouped[['Goals','GoalsPerGame']].aggregate(min)
grouped[['Goals','GoalsPerGame']].aggregate(sum)
grouped[['Goals','GoalsPerGame']].aggregate(np.median)

grouped.aggregate(np.median)

## .apply()  -- synonym
grouped['GoalsPerGame'].apply(np.max)

#%%
'''
Matching operators
------------------

R's %in% vs pandes' isin()
'''

stocks_df.Symbol

stocks_df.Symbol.isin(['GOOG','AAPL'])

stocks_df['Price']>200

#%%
'''
Logical subsetting
------------------
'''

stocks_df.Symbol[stocks_df.Symbol.isin(['GOOG','AAPL'])]

stocks_df[stocks_df['Price']>200]

stocks_df[stocks_df['Symbol']=='GOOG']

stocks_df.query('Price>200')

stocks_df.query("Symbol=='GOOG'")
stocks_df.query('Symbol=="GOOG"')

#%%
'''
Split-apply-combine
-------------------

`plyr` package in R
> ddply( flights.sample, .(year, month), summarise,
         mean_dep_delay = round(mean(dep_delay),2),
         sd_dep_delay = round(sd(dep_delay),2)
       )
'''

flights_sample = pd.read_csv( 'nycflights13_sample.csv' )

flights_sample.head()
flights_sample.head(20)
flights_sample.tail()
flights_sample.shape
flights_sample.size
type(flights_sample)  ## pandas.core.frame.DataFrame


#%%

pd.set_option('precision',3)
pd.options

grouped = flights_sample.groupby(['year','month'])
type(grouped)  ## pandas.core.groupby.DataFrameGroupBy

grouped.agg(np.mean)
grouped.agg([np.mean,np.std])
grouped.agg([np.mean,np.std,np.median])

grouped['dep_delay'].agg([np.mean,np.std,np.median])


#%%
'''
Reshaping usng melt()
---------------------

    http://www.statmethods.net/management/reshape.html.
    http://pandas.pydata.org/pandasdocs/stable/reshaping.html#reshaping-by-melt.

> melt(...)
'''

flights4 = flights_sample[['year','month','dep_delay','arr_delay']].head(4)
flights4

pd.melt(flights4, id_vars=['year','month'])

#%%
'''
Factors/categorical data
------------------------

> cut()
'''

pd.set_option('precision', 4)

clinical = pd.DataFrame( { 'patient' : range(1,1001) ,
                           'age' : np.random.normal(50,5,size=1000) ,
                           'year_enroll' : [ str(x) for x in np.random.choice( range(1980,2000), size=1000, replace=True ) ]
                         } )

clinical.head(10)
clinical.tail(10)

clinical.describe()
clinical.describe(include=['object'])   ## ?

clinical.year_enroll.value_counts()[:6]
clinical.year_enroll.value_counts().head(10)

agecut = pd.cut( clinical['age'] , 5 )
agecut
agecut.head()
type(agecut)        ## pandas.core.series.Series
type(agecut[0])        ## pandas.core.series.Series

agecut.value_counts().sort_index()

#%%
clinical.dtypes

clinagecut = pd.cut( clinical['age'], bins = [0, 20, 50, 70, 90, 100]
                       , labels = [str(x) for x in range(5)] 
                       , right=True)

clinical['age_cut'] = clinagecut.
type(clinagecut[0])

ye = pd.Series([int(x) for x in clinical['year_enroll']])
ye.describe()
clinyearcut = pd.cut( ye, bins = [1979, 1985, 1990, 1995, 2000]
                       , labels = [str(x) for x in range(4)] 
                       , right=True)

clinical['ye_cut'] = clinyearcut.astype()
clinical['ageyear'] = clinical['age_cut'].astype(str) + clinical['ye_cut'].astype(str)
clinical['ageyear_tup'] = clinical['age_cut'].astype(str), clinical['ye_cut'].astype(str)

clinical[['age_cut','ye_cut']].apply( lambda x: (x[0], x[1]), axis=1)
clinical[['age_cut','ye_cut']].apply( lambda x: tuple(x), axis=1)

clinical['ageye_cut'] = [ x for x in  zip(clinagecut.astype(int), clinyearcut.astype(int)) ]  ## OK, tuples
clinical['ageye_cut'] =  zip(clinagecut.astype(int), clinyearcut.astype(int))   ### NO!!!!

clinical['ageye_cut'][0][0]
type(clinical['ageye_cut'][0][0])


pd.cut()