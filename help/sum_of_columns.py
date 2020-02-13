# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 10:15:58 2018

@author: akasprzy
"""

lst = [(1,2,3), (2,5,6), (3,8,5), (1,5,7), (1,3,8), (2,6,4), (2,0,1), (3,2,5), (3,6,2)]  ## (floor, x, y)

#%% 1st
def sumi(lst, i):
    return sum( [ l[i] for l in lst ] )

def nth_floor(lst, n):
    return [ l for l in lst if l[0]==1 ]
    
[ [n] + [ sumi( nth_floor(lst,n), i) for i in [1,2]  ] ## [1,2]==[x,y]
  for n in [1,2,3]  ## floors
]

#%% 2nd

df = pd.DataFrame(lst)
dfg = df.groupby(0)
dfg[[1,2]].aggregate(sum)

#%% 3d

lst
list( filter(lambda x: x[0]==1, lst) )


[ filter(lambda x: x[0]==floor, lst) for floor in [1, 2, 3] ]


np.array( list( filter(lambda x: x[0]==1, lst) ) ).sum(axis=0)




    

    

