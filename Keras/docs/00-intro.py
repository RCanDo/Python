# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:32:19 2019

https://keras.io/

author: kasprark
email: arkadiusz.kasprzyk@tieto.com
"""


import keras
from keras.models import Sequential


#%%

model = Sequential()
model


#%%

from keras.layers import Dense

model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))

model

#%% .compile()
"""
!!!
Once your model looks good, configure its learning process with .compile():
"""
    
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

model

#%% more refined

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True))

model
model.summary()

#%% You can now iterate on your training data in batches:

# x_train and y_train are Numpy arrays -- just like in the Scikit-Learn API.

model.fit(x_train, y_train, epochs=5, batch_size=32)


#%% Alternatively, you can feed batches to your model manually:

model.train_on_batch(x_batch, y_batch)


#%% Evaluate your performance in one line:

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)


#%% Or generate predictions on new data:

classes = model.predict(x_test, batch_size=128)



