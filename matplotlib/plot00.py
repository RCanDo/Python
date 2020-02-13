# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 09:02:47 2018

@author: akasprzy
"""

import matplotlib as mpl
import matplotlib.pyplot as plt

#%%
pl.figure( num=None
         , figsize=None
         , dpi=None
         , facecolor=None
         , edgecolor=None
         , frameon=True
         , FigureClass=<class 'matplotlib.figure.Figure'>
         , clear=False
         , **kwargs
         )

#%%
mpl.rcParams

plt.style.available
mpl.get_configdir()

plt.close('all')

#%%

plt.figure(figsize=(2,3), facecolor='black', edgecolor='red')
plt.plot([1,2,3],[3,1,2])
#%%

print(plt.style.available)

#%%
plt.style.use('dark_background')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1,2,3],[3,1,2])

#%%
plt.style.use(PATH['wd']+'/ak_basic.mplstyle')

fig = plt.figure()

ax = fig.add_subplot(111)
ax.plot([1,2,3],[3,1,2])
ax.plot([1,2,3],[2,1,3])
ax.plot([1,2,3],[2,3,1])

ax.locator_params()

ax.grid()

ax.set_xlabel("x") #, fontsize = 7)
ax.set_ylabel("y")

#plt.title("some plots")
ax.set_title("some plots")

#plt.tight_layout()
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=.5)                ## fraction of fontsize
#plt.subplots_adjust(left=0.03, right=0.97, top=0.97, bottom=0.03)   ## fraction of a figure  


#%%


