# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Wed Dec 13 11:16:15 2017

12. List comprehension
======================
"""

#%%

[2**i for i in range(10)]

[x**2 for x in range(10)]

[x for x in range(10) if x > 5]

#%%

xs = [i for i in range(10)]
xs

ys = [x**2 for x in xs]
ys

#%%
import math as m

ys = [m.exp(x) for x in xs]
ys

xs = [n/10 for n in range(4)]
xs

ys  ## ys is already generated so the change in xs definition doesn't change ys

## you must run it again
ys = [m.exp(x) for x in xs]
ys

ys = [m.exp(x) for x in xs]
ys

words = 'The quick brown fox jumps over the lazy dog'.split()
words

stuff = [ [w.upper(), w.lower(), len(w) ] for w in words ]
stuff

for s in stuff:
    print(s)

for s in stuff:
    print("{:10s}, {:10s}, {:10d}".format(s))           ## ERROR

for s in stuff:
    print("{:10s}, {:10s}, {:10d}".format(tuple(s)))    ## TypeError: unsupported format string passed to tuple.__format__

for s in stuff:
    print("{:10s}, {:10s}, {:10d}".format(s[0],s[1],s[2]))    ## OK!  but this is tediuos and not scaleable...

for s in stuff:
    print("%10s, %10s, %10d" % tuple(s))    ## OK!  but this is old type of formatting; still better then new



#%%
## generating float series
## with given limits

[x*.2 for x in range(10)]    ## only step given but upper limit or number of elements to be derived

[x*.2 for x in range(3,10)]    ## only step given but lower and upper limit or number of elements to be derived

## 1. step given,  e.g.=.2

[x*.2 for x in range(round(10/.2))]     ## 10 is upper limit

[3 + x*.2 for x in range(round((10-3)/.2))]         ## {3, 3.2, 3.4, ..., 9.8}
[3 + x*.2 for x in range(round((10-3)/.2) + 1)]     ## {3, 3.2, 3.4, ..., 9.8, 10}

[-3 + x*.2 for x in range(round((10-(-3))/.2))]         ## {-3, -2.8, -2.6, ..., 9.8}
[-3 + x*.2 for x in range(round((10-(-3))/.2) + 1)]     ## {-3, -2.8, -2.6, ..., 9.8, 10}


## 2. number of elements given,  e.g.=8

## lower limit default,  i.e.=0
[0 + x*10/8 for x in range(8)]          ## 8 elements from 0 to 10 but without 10
[0 + x*10/8 for x in range(8+1)]        ## 8 elements from 0 to 10 but without 10  + {10}  =  9 elements

[0 + x*10/7 for x in range(8)]          ## 7 elements from 0 to 10 but without 10  + {10}  =  8 elements

## lower limit given,  e.g.=3
[3 + x*(10-3)/8 for x in range(8)]          ## 8 elements from 3 to 10 but without 10
[3 + x*(10-3)/8 for x in range(8+1)]        ## 8 elements from 3 to 10 but without 10  +  {10}  =  9 elements

[3 + x*(10-3)/7 for x in range(8)]          ## 7 elements from 3 to 10 but without 10  + {10}  =  8 elements

## lower limit given,  e.g.=-3
[-3 + x*(10+3)/8 for x in range(8)]          ## 8 elements from 3 to 10 but without 10
[-3 + x*(10+3)/8 for x in range(8+1)]        ## 8 elements from 3 to 10 but without 10  +  {10}  =  9 elements

[-3 + x*(10+3)/7 for x in range(8)]          ## 7 elements from 3 to 10 but without 10  + {10}  =  8 elements

#%%





