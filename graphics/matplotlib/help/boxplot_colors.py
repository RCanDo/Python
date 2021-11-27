# -*- coding: utf-8 -*-
#! python3
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Python Matplotlib Boxplot Color
version: 1.0
type: example
keywords: [boxplot]
description: |
remarks:
todo:
sources:
    - title: Python Matplotlib Boxplot Color
      link: https://stackoverflow.com/questions/41997493/python-matplotlib-boxplot-color/41997865
file:
    usage:
        interactive: True
        terminal: False
    date: 2021-11-13
    authors:
        - fullname: Arkadiusz Kasprzyk
          email:
              - arek@staart.pl
"""

#%%
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
# plt.style.use('grayscale')
# plt.style.available

#%%
"""
To colorize the boxplot, you need to first use the `patch_artist=True` keyword
to tell it that the boxes are patches and not just paths.
Then you have two main options here:

1. Set the color via `...props` keyword argument, e.g.
    `boxprops=dict(facecolor="red")`
    For all keyword arguments, refer to the documentation.

2. Use the `plt.setp(item, properties)` functionality
    to set the properties of the boxes, whiskers, fliers, medians, caps.

3. Obtain the individual items of the boxes from the returned dictionary
    and use `item.set_<property>(...)` on them individually.
    This option is detailed in an answer to the following question:
    [python matplotlib filled boxplots](https://stackoverflow.com/questions/20289091/python-matplotlib-filled-boxplots),
    where it allows to change the color of the individual boxes separately.
"""
#%%  The complete example, showing options 1 and 2:
data = np.random.normal(0.1, size=(100, 6))
data[76:79,:] = np.ones((3,6)) + 0.2     # outliers

plt.figure(figsize=(4,4))

#%% option 1, specify props dictionaries
plt.boxplot(data[:,::2],
            positions=[1,2,3],
            notch=True,
            #
            patch_artist = True,                              #!!!
            boxprops = dict(color="blue", facecolor="red"),
            whiskerprops = dict(color="orange"),
            capprops = dict(color="green"),
            flierprops = dict(color="grey", markeredgecolor="black", marker="D"),
            medianprops = dict(color="white"),
            )

#%% option 2, set all colors individually
box1 = plt.boxplot(data[:,::-2] + 1,           #!!!   + 1
                   positions=[1.5,2.5,3.5],
                   notch=True,
                   patch_artist=True)

items = ['boxes', 'whiskers', 'caps', 'fliers', 'medians']
colors = ['blue', 'orange', 'green', 'grey', 'white']

for i, c in zip(items, colors):
    plt.setp( box1[i], color=c )

plt.setp(box1["boxes"], facecolor='red')
plt.setp(box1["fliers"], markeredgecolor='black', marker="_")


plt.xlim(0.5,4)
plt.xticks([1,2,3], [1,2,3])
plt.show()

#%%
xx = np.random.randint(0, 36, size=[6, 6])
xx

xx[:,::2]
xx[:,::-2]
xx[:,:2:-1]
xx[:,-2::]

#%%