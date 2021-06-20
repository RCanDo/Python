# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 10:03:51 2021

@author: staar
"""
#%% 3. Memory
"""
This snippet can be used to check the memory usage of an object.
"""
import sys
variable = 30
sys.getsizeof(variable) # 28

#%% 4. Byte size
"""
This method returns the length of a string in bytes.
"""
def byte_size(string):
    return(len(string.encode('utf-8')))

byte_size('Hello world!')  # 12
byte_size('😀')  # 4

#%%
#%%
# 8. Measure the execution time of small bits of Python code with the "timeit" module

# The "timeit" module lets you measure the execution
# time of small bits of Python code

import timeit

"-".join(str(n) for n in range(100))
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# 0.3412662749997253

"-".join([str(n) for n in range(100)])
timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
# 0.2996307989997149

"-".join(map(str, range(100)))
timeit.timeit('"-".join(map(str, range(100)))', number=10000)
# 0.24581470699922647

#%% 22. Time spent
"""
This snippet can be used to calculate the time it takes to execute
a particular code.
"""
import time
start_time = time.time()
a=1
b=2
c=a+b
print(c)
end_time = time.time()
total_time = end_time - start_time

print("Time: ", total_time)

#%% %timeit -- IPython magic command
import numpy as np
arr = np.arange(1000)
%timeit arr**3
# 2.73 µs ± 53.7 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

arr = range(1000)
%timeit [i**3 for i in arr]
# 326 µs ± 11.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

#%%

