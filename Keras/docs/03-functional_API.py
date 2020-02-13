# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 21:01:56 2019

https://keras.io/getting-started/functional-api-guide/

author: kasprark
email: arkadiusz.kasprzyk@tieto.com
"""

"""
Getting started with the Keras functional API
=============================================

The Keras functional API is the way to go for defining complex models, such as 
    multi-output models, 
    directed acyclic graphs, or 
    models with shared layers.

This guide assumes that you are already familiar with the Sequential model.

Let's start with something simple.



First example: a densely-connected network
------------------------------------------

https://keras.io/getting-started/functional-api-guide/#first-example-a-densely-connected-network

The Sequential model is probably a better choice to implement such a network, 
but it helps to start with something really simple.

    A layer instance is callable (on a tensor), and it returns a tensor.
    Input tensor(s) and output tensor(s) can then be used to define a Model.
    Such a model can be trained just like Keras Sequential models.

"""



#%%

from keras.layers import Input, Dense
from keras.models import Model

from keras import utils
import numpy as np

#%% for tensorboard

import os
import glob

os.chdir("D:\\ROBOCZY\\Python\\Keras\\")
for file in glob.glob(".\\events*"):
    os.remove(file)
    
import tensorflow.summary as tfs
from tensorflow import get_default_graph as gdg

writer = tfs.FileWriter(".")

writer.add_graph(gdg())

#%%

# This return a tensor

inputs = Input(shape=(100,))

# a layer instance is callable on a tensor and returns a tensor
x = Dense(64, activation='relu')(inputs)
x = Dense(64, activation='relu')(x)
predictions = Dense(10, activation='softmax')(x)

# the model including the Input and three Dense layers
model = Model(inputs=inputs, outputs=predictions)
model.compile(optimizer='rmsprop', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])
model.summary()

writer.add_graph(gdg())

#%% dummy data

data = np.random.random((1000, 100))
labels = np.random.randint(10, size=(1000, 1))
labels = utils.to_categorical(labels, num_classes=10)    # one_hot_labels

model.fit(data, labels, epochs=10, batch_size=32)  # starts training

import keras.backend as K
model.weights
print(K.eval(model.weights[1]))

model.predict(data)

#! plot it somehow ?

#%% 
"""
All models are callable, just like layers
-----------------------------------------

https://keras.io/getting-started/functional-api-guide/#all-models-are-callable-just-like-layers

With the functional API, it is easy to reuse trained models: 
you can treat any model as if it were a layer, by calling it on a tensor. 
Note that by calling a model you aren't just reusing the architecture of the model, 
you are also reusing its weights.
"""

x = Input(shape=(100,))
# This works, and returns the 10-way softmax we defined above.
y = model(x)

"""
This can allow, for instance, to quickly create models that can process sequences of inputs. 
You could turn an image classification model into a video classification model, 
in just one line.
"""

from keras.layers import TimeDistributed

# Input tensor for sequences of 20 timesteps,
# each containing a 100-dimensional vector
input_sequences = Input(shape=(20, 100))

# This applies our previous model to every timestep in the input sequences.
# the output of the previous model was a 10-way softmax,
# so the output of the layer below will be a sequence of 20 vectors of size 10.
processed_sequences = TimeDistributed(model)(input_sequences)


#%%  Multi-input and multi-output models
# https://keras.io/getting-started/functional-api-guide/#multi-input-and-multi-output-models







