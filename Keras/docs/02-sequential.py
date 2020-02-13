# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:55:42 2019

https://keras.io/getting-started/sequential-model-guide/

author: kasprark
email: arkadiusz.kasprzyk@tieto.com
"""

%reset

#%%

import keras
import keras.backend as K

from keras.models import Sequential
from keras.layers import Dense, Activation

import numpy as np


#%% 
"""
The Sequential model is a linear stack of layers.
You can create a Sequential model by passing a list of layer instances to the constructor:
"""

model = Sequential([
            Dense(32, input_shape=(784,)),
            Activation('relu'),
            Dense(10),
            Activation('softmax')
        ])
    
model    
model.summary()

#%%

model.evaluate()   # ValueError: If evaluating from data tensors, you should specify the `steps` argument.

K.eval(model)      # AttributeError: 'Sequential' object has no attribute 'eval'

    
#%% You can also simply add layers via the .add() method:
   
model = Sequential()
model.add(Dense(32, input_dim=784))
model.add(Activation('relu'))

model.summary()

#%%  the following snippets are strictly equivalent:
   
model = Sequential()
model.add(Dense(32, input_dim=784))

model = Sequential()
model.add(Dense(32, input_shape=(784,)))

model.weights
model.weights[1]
K.eval(model.weights[1])

#%% Compilation

# for multi-class classification problelm
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# for a binary classification problem
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# for a mean squared error regression problem
model.compile(optimizer='rmsprop',
              loss='mse')

#%%
# for custom metrics

"""
metrics must take two arguments
    y_true: True labels. Theano/TensorFlow tensor.
    y_pred: Predictions. Theano/TensorFlow tensor of the same shape as y_true.
"""

def mean_pred(y_true, y_pred):
    return K.mean(y_pred)

y_true = np.array([1, 2, 3])
y_pred = np.array([.2, 1.3, 3.1])

mean_pred(y_true, y_pred)   #! AttributeError: 'numpy.dtype' object has no attribute 'base_dtype'
K.mean(y_pred)              #! AttributeError: 'numpy.dtype' object has no attribute 'base_dtype'

"""
so y_true and y_pred must be turned to tf.tensor 
"""
from tensorflow import constant

K.mean(constant(y_pred))

K.eval(K.mean(constant(y_pred)))
K.eval(mean_pred(constant(y_true), constant(y_pred)))

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy', mean_pred])

#%% Training

# binary classification

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

# dummy data
data = np.random.random((1000, 100))
labels = np.random.randint(2, size=(1000, 1))

# train the model, iterating on the data in batches of 32 samples
model.fit(data, labels, epochs=10, batch_size=32)

# model.train(data, labels, epochs=10, batch_size=32)    
  # ! AttributeError: 'Sequential' object has no attribute 'train'

pred = model.predict(data)
pred
type(pred)
pred.shape

model.weights
model.weights[1]
K.eval(model.weights[1])

model.weights[0]
K.eval(model.weights[0]).shape

K.eval(model.output)



#%%

# categorical classification - 10 classes

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()

# dummy data
data = np.random.random((1000, 100))
labels = np.random.randint(10, size=(1000, 1))

# convert labels to categorical one-hot encoding
one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)

# train the model...
model.fit(data, one_hot_labels, epochs=10, batch_size=32)
one_hot_labels[range(5), :]

predict = model.predict(data)
predict.shape


#%%

mse = keras.losses.mean_squared_error(labels, predict)
K.eval(mse)  # ???


mmse = keras.metrics.mean_squared_error(labels, predict)
K.eval(mmse)


#%%

import tensorflow.keras as tfk

dir(tfk.losses)

tfmse = tfk.losses.MeanSquaredError()  #!! #! AttributeError: module 'tensorflow._api.v1.keras.losses' has no attribute 'MeanSquaredError'

tfmse = tfk.losses.mean_squared_error(labels, predict)
tfmse

tfmse = tfk.losses.mse(labels, predict)
tfmse

tfmmse = tfk.metrics.mse(labels, predict)
tfmmse




#%%
#%% EXAMPLES

#%% 1. Multilayer Perceptron (MLP) for multi-class softmax classification