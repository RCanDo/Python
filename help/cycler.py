# -*- coding: utf-8 -*-
"""
title: cycler()
doc: https://matplotlib.org/cycler/#examples
author: akasprzy
date: Sat Mar  3 09:01:12 2018
"""

%reset

#%%
from cycler import cycler

## addition
cc = ( cycler(color=list('rgb')) + cycler(linestyle=['-','--','- ']) )
cc
for d in cc: print(d)

## multiplication
cc = cycler(color=list('rgb')) * cycler(linestyle=['-','--','- '])
cc
for d in cc: print(d)

#%% from the beginning
#%%

col_c = cycler(color=list('rgb'))
col_c
for c in col_c: print(c)

## changing key
col2_c = cycler(ec=col_c)
for c in col2_c: print(c)

#%% Iterating over a Cycler results in the finite list of entries, 
##  to get an infinite cycle, call the Cycler object (a-la a generator)

col_gen = col_c()
col_gen

for j, c in zip(range(7), col_gen):   print(j, c)
for j, c in zip(range(27), col_gen):   print(j, c)

for k in col_gen: print(k)      ## Oooops: infinite loop...

#%% Composition of cyclers

lw_c = cycler(lw=range(1,4))
for c in lw_c: print(c)

col_c + lw_c
for k in col_c + lw_c: print(k)

#%% 
ca = cycler(a=range(2))
cb = cycler(b=range(3))

for k in ca+cb: print(k)  ## ValueError: Can only add equal length cycles, not 2 and 3     !!!!   Sadly...

#%% addition is commutative

for k in col_c + lw_c: print(k)
for k in lw_c + col_c: print(k)

for j, (a, b) in enumerate(zip(col_c + lw_c, lw_c + col_c)):
    print('({j}) A: {A!r}  B: {B!r}'.format(j=j, A=a, B=b))

for j, (a, b) in enumerate(zip(col_c + lw_c, lw_c + col_c)):
    print('{j} {A} {B}'.format(j=j, A=a, B=b))
   

#%% instead of addition it is possible to pass multiple key-value pairs
    
colw_c = cycler(col=list('rgb'), lw=range(3))
for s in colw_c:  print(s)    

cycler(col=list('rgb'), lw=range(4))  ## ValueError: Can only add equal length cycles, not 3 and 4

## you may use zip() but it prunes to smaller cycle...
cc3 = cycler(col=list('rgb'))
cc4 = cycler(lw=range(4))

zz24 = zip(cc3, cc4)
for i in zz24: print(i)

zz43 = zip(cc4, cc3)
for i in zz43: print(i)

for k in zip(range(4), cc3): print(k)  ## the same...

#%% use 
from itertools import cycle

for k in zip(cc4, cycle(cc3)): print(k)
for k in zip(cycle(cc4), cc3): print(k)  ##!!!! pruned to cc2
for k in zip(range(4), cycle(cc3)): print(k)
for k in zip(cycle(cc4), cycle(cc3)): print(k)  ##!!!! Ooooops... INFINTE LOOP!!!

#%% multiplying of cycles

mark_c = cycler(m=list('so'))
colmark_c = col_c * mark_c
colmark_c
for c in colmark_c: print(c)

## not commutative (but the same set of results)
markcol_c = mark_c * col_c
for c in markcol_c : print(c)

## replacing keys:
colmark_c.keys
colmark_c.keys = {'color', 'marker'}  ## AttributeError: can't set attribute
## so you can't...


#%% multiplication by integer

col_c
col_c*3
for c in col_c*3: print(c)

#%% concatenation

## via method
col_c.concat(col_c)
## but keys MUST be the same

col_c.concat(mark_c) ## ValueError: Keys do not match:

## or via 
from cycler import concat
concat(col_c,col_c)

#%% slicing
col_c
col_c[::-1]
col_c[:2]
col_c[1:]

#%% Inspecting the Cycler
col_c              ## cycler
type(col_c)
len(col_c)

col_d = col_c.by_key()      ## making dict from cycler
col_d
type(col_d)

## This dict can be mutated and used to create a new Cycler with the updated values

col_d['color'] = ['green'] * len(col2_c)
col_d

cycler(**col_d)

#%% with two keys

colmark_c
colmark_d = colmark_c.by_key()  ## making dict from cycler
colmark_d

colmark_d['color'] = list('cmy')*2
colmark_d

cm_c = cycler(**colmark_d)
for k in cm_c: print(k)

#%%
#%% Examples

#import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler
from itertools import cycle
plt.close("all")

#%%
fig, (ax1, ax2) = plt.subplots(1, 2, tight_layout=True, figsize=(8,4))
fig
x = np.arange(10)

col_c = cycler(c=list('rgb'))
for i in enumerate(col_c): print(i)

for i, sty in enumerate(col_c):  ax1.plot(x, x*(i+1), **sty)
    
for i, sty in zip(range(1, 5), cycle(col_c)):  ax2.plot(x, x*i, **sty)
    
#%% !!!!!!   
for k in zip(range(5), cycle(col_c)): print(k)

#%%
fig, ax = plt.subplots(1, 2, tight_layout=True, figsize=(8,4))
ax

ls_c = cycler('ls', ['-','--'])
lw_c = cycler('lw', range(1,4))

sty_c = ls_c * (col_c + lw_c)
for s in sty_c: print(s)

for i, sty in enumerate(sty_c):  ax[0].plot(x, x*(i+1), **sty)
    
sty_c = (col_c + lw_c) * ls_c
for s in sty_c: print(s)

for i, sty in enumerate(sty_c):
    ax[1].plot(x, x*(i+1), **sty)
    
#%% persistent cycles
'''
It can be useful to associate a given label with a style via dictionary lookup and to dynamically generate that mapping. 
This can easily be accomplished using a defaultdict
'''
    
from collections import defaultdict

cw_c = col_c + lw_c
cw_c
for c in cw_c: print(c)

## To get a finite set of styles
cw_iter = iter(cw_c)
cw_iter
for i in cw_iter: print(i)

cw_dic = defaultdict(lambda: next(cw_iter))
cw_dic
for d in cw_dic: print(d)

## or repeating
cw_c()
dd_loop = defaultdict(lambda: next(cw_c()))
dd_loop
for d in dd_loop: print(d)

## This can be helpful when plotting complex data which has both a classification and a label

fig, ax = plt.subplots(tight_layout=True)
for group, label, data in DataSet:                ## DataSet ???
    ax.plot(data, label=label, **cw_dic[group])

#%% Motivation
'''
When plotting more than one line it is common to want to be able to cycle over one or more artist styles. 
For simple cases this can be done without too much trouble:
'''
x = np.linspace(0, 2*np.pi, 1024)

fig, ax = plt.subplots(tight_layout=True)

for i, (lw, c) in enumerate(zip(range(4), list('rgbk'))): ##print(i,lw,c)
    ax.plot( x, np.sin(x-i*np.pi/4)
            , label=r'$\phi - {{{0}}}\pi / 4$'.format(i)
            , lw = lw + 1
            , c = c )

ax.set_xlim([0, 2*np.pi])
ax.set_title(r'$y=\sin(\theta+\phi)$')
ax.set_ylabel(r'[arb]')
ax.set_xlabel(r'$\theta$ [rad]')

ax.legend(loc=0)            

#%%
'''However, if you want to do something more complicated:
'''
x = np.linspace(0, 2*np.pi, 1024)

fig, ax = plt.subplots(tight_layout=True)

for i, (lw, c) in enumerate(zip(range(4), list('rgbk'))): ##print(i,lw,c)
    if i % 2 == 0:
        ls = '-'
    else:
        ls = '--'
    ax.plot( x, np.sin(x-i*np.pi/4)
            , label=r'$\phi - {{{0}}}\pi / 4$'.format(i)
            , lw = lw + 1
            , c = c 
            , ls = ls
           )

ax.set_xlim([0, 2*np.pi])
ax.set_title(r'$y=\sin(\theta+\phi)$')
ax.set_ylabel(r'[arb]')
ax.set_xlabel(r'$\theta$ [rad]')

ax.legend(loc=0)

'''
the plotting logic can quickly become very involved. 
To address this and allow easy cycling over arbitrary kwargs the Cycler class, a composable kwarg iterator, 
was developed.
'''
#%% the same using cycler()

x = np.linspace(0, 2*np.pi, 1024)
fig, ax = plt.subplots(tight_layout=True)

pars = cycler(lw = range(1,5), c = list('rgbk'), ls = ['-','--']*2)
for p in pars: print(p)

for i, sty in enumerate(pars):       ## we need i
    ax.plot( x, np.sin(x-i*np.pi/4)  
            , label=r'$\phi - {{{0}}}\pi / 4$'.format(i) 
            , **sty
           )

ax.set_xlim([0, 2*np.pi])
ax.set_title(r'$y=\sin(\theta+\phi)$')
ax.set_ylabel(r'[arb]')
ax.set_xlabel(r'$\theta$ [rad]')

ax.legend(loc=0)

#%% try to pack all parameters into cycler:




