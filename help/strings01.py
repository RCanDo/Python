"""
see also ./PFCSAE/pfcsae-sl-07
"""
#%%
str.center()
str.zfill()
str.ljust()
str.rjust()
str.upper()
str.capitalize()
str.count()
str.endswith()
str.split()
str.startswith()
...

#%%
f'{2*3}'

name = 'LEOnarDO'
f'{name.lower()}'

f'{" ".join(list("abcd"))}'

#%%
'''
7.1 Fancier Output Formatting
-----------------------------
'''
#%% .rjust()

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(4), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(5))

'''
Note that in the first example, one space between each column was added by the way print() works:
it always adds spaces between its arguments.
'''
#%%
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

#%% .ljust()

for x in range(1, 11):
    print(repr(x).ljust(2), repr(x*x).ljust(4), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).ljust(5))

#%%
for x in range(1, 11):
    print('{0:1d} {1:1d} {2:1d}'.format(x, x*x, x*x*x))   ## ????

#%%

"very_long_string".ljust(8)[:8]

#%% .center()

for x in range(1, 20):
    print(repr(x).center(2), repr(x*x).center(4), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).center(5))

#%%
for k in range(1,10):
    print(repr(int(eval("1e"+str(k)))).center(9))
#%%
#%%

r = range(256)
for i in r: print(i)

#%%
#%%

import math as m

#%%
def print_fun_tab(xx,f):
    for x in xx:
        print("{}({:7.2f}) = {:7.2f} ".format(f.__name__, x, f(x)))

xx = range(-3,3)
print_fun_tab(xx, m.sin)

#%%
string = "qq"
fl = float(10)
d = 10

if isinstance(string,str):
    print("String %s" % string)
if isinstance(fl,float):
    print("Float %f" % fl)
if isinstance(d,int):
    print("Integer %d" % d)

#%%
