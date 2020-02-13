# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:12:04 2019

https://keras.io/backend/

author: kasprark
email: arkadiusz.kasprzyk@tieto.com
"""

#%% 

import numpy as np
from keras import backend as K

import tensorflow as tf

#%%

K.backend()

#%%  
"""
The code below instantiates an input `placeholder`. 
It's equivalent to tf.placeholder() or tf.tensor.matrix(), tf.tensor.tensor3(), etc.
"""

inputs = K.placeholder(shape=(2, 4, 5))
inputs

inputs = K.placeholder(shape=(None, 4, 5))
inputs

inputs = K.placeholder(ndim=3)
inputs

#%%

val = np.random.random((2, 3, 4))
val

var = K.variable(value=val)
var

#%% In Keras as in TensorFlow to see the results you must first evaluate it:

var  # just some meta info about object\

# to see its value you must evaluate it
K.eval(var)


#%%  via TensorFlow it's more complicated as one must create a `session` first

ss = tf.Session()
ss

init = tf.global_variables_initializer()  # and variables need to be initialized
ss.run(init)
print(ss.run(var))


#%%

var = K.zeros(shape=(3, 4, 5))
var
K.eval(var)

# via TF
ss.run(tf.global_variables_initializer())
ss.run(var)
#%%

var = K.ones(shape=(3, 4, 5))
var
K.eval(var)

#%%

K.clear_session()

# Initializing Tensors with Random Numbers
b = K.random_uniform_variable(shape=(3, 4), low=0, high=1) # Uniform distribution
c = K.random_normal_variable(shape=(3, 4), mean=0, scale=1) # Gaussian distribution
d = K.random_normal_variable(shape=(3, 4), mean=0, scale=1)

for l in (b, c, d): print(K.eval(l))

list(map(lambda x: K.eval(x), [b, c, d]))


#%%
# Tensor Arithmetic

a = b + c * K.abs(d)
f = K.dot(a, K.transpose(b))
g = K.sum(b, axis=1)
h = K.softmax(b)
k = K.concatenate([b, c], axis=-1)

for l in (a, f, g, h, k): print(K.eval(l))


#%% ...

K.clear_session()

var = K.variable([[1, 2, 3], [4, 5, 6]])
K.eval(var)

var_transposed = K.transpose(var)
K.eval(var_transposed)

inputs = K.placeholder((2, 3))
inputs
input_transposed = K.transpose(inputs)
input_transposed


K.eval(input_transposed)  # ooops...


#%%     

K.epsilon()

#%%






