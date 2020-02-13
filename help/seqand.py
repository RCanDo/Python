# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:07:28 2018

@author: akasprzy
"""

import random

#%%
def seqand( df, varnames, conds):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(varnames)):
        exec("{} = df.{}".format(letters[i], varnames[i]))
    
    res = pd.Series( [True] * len(a) ) 
    
    for c in conds:
        cond = "res & ({:s})".format(c)
        #res = eval(compile("res = res & ({:s})".format(c), '<string>', 'single'))
        res = eval( cond )
        
    return res        

#%%
    
df = pd.DataFrame({ 'var1' : np.random.randn(5), 'var2' : np.random.randn(5), 'var3' : np.random.randn(5) })
df
exec('b = df.var2')
exec('res = (res & (b > 0))')
res

seqand(df, ['var1','var2'], ['a>0','b<0'] )
    
a = np.random.randn(5)  
exec('b = a>0')
b
"{} = df.{}".format('a', 'variab')
"res = {}".format('a>0')


eval(compile('z = -np.pi*2', '<string>', 'single'))
z
