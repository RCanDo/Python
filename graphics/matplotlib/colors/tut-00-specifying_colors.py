#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Specifying Colors
subtitle:
version: 1.0
type: tutorial
keywords: [color]
description: |
    About colors in matplotlib.
remarks:
    - etc.
todo:
    - problem 1
sources:
    - title: Specifying Colors
      link: https://matplotlib.org/stable/tutorials/colors/colors.html
    - title: List of named colors
      link: https://matplotlib.org/stable/gallery/color/named_colors.html
      remark: !!!
    - title: Colors
      link: https://matplotlib.org/stable/gallery/index.html#color
      usage: |
          Get into each example...
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: E:/ROBOCZY/Python/graphics/matplotlib/colors/
    date: 2021-10-04
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""
#%%
import os, json

#%%
ROOT = json.load(open('root.json'))
WD = os.path.join(ROOT['Works'], "Python/graphics/matplotlib/")   #!!! adjust
os.chdir(WD)

#%%
WD = os.getcwd()
print(WD)

#%%
import numpy as np
import pandas as pd

#%%
#%%
import matplotlib as mpl
import matplotlib.pyplot as plt
# plt.style.use('dark_background')
# see `plt.style.available` for list of available styles

#%%
#%%  Colors - Example 1: Color Demo
##   https://matplotlib.org/stable/gallery/color/color_demo.html#sphx-glr-gallery-color-color-demo-py
#
t = np.linspace(0.0, 2.0, 201)
s = np.sin(2 * np.pi * t)

# 1) RGB tuple:
fig, ax = plt.subplots(facecolor=(.18, .31, .31))

# 2) hex string:
ax.set_facecolor('#eafff5')

# 3) gray level string:
ax.set_title('Voltage vs. time chart', color='0.7')

# 4) single letter color string
ax.set_xlabel('time (s)', color='c')

# 5) a named color:
ax.set_ylabel('voltage (mV)', color='peachpuff')

# 6) a named xkcd color:
ax.plot(t, s, 'xkcd:crimson')

# 7) Cn notation:
ax.plot(t, .7*s, color='C4', linestyle='--')

# 8) tab notation (Tableau Colors from 'T10' categorical palette):
ax.tick_params(labelcolor='tab:orange')

plt.show()

#%%
#%% Specifying Colors
##!!!   https://matplotlib.org/stable/tutorials/colors/colors.html   !!!
## tables of basic color names there;
## together with different ways of specifing colors.

#%%
"""
Matplotlib recognizes the following formats in the table below to specify a color.

Format                                                              Example
-----------------------------------------------------------------   --------------------
RGB or RGBA (red, green, blue, alpha) tuple of float values
in a closed interval [0, 1].
                                                                    (0.1, 0.2, 0.5)
                                                                    (0.1, 0.2, 0.5, 0.3)
Case-insensitive hex RGB or RGBA string.
                                                                    '#0f0f0f'
                                                                    '#0f0f0f80'
Case-insensitive RGB or RGBA string equivalent hex shorthand
of duplicated characters.
                                                                    '#abc' as '#aabbcc'
                                                                    '#fb1' as '#ffbb11'
String representation of float value in closed interval [0, 1]
for black and white, respectively.
                                                                    '0.8' as light gray
                                                                    '0' as black
                                                                    '1' as white
Single character shorthand notation for shades of colors.
 Note
The colors green, cyan, magenta, and yellow
do not coincide with  X11/CSS4  colors.
                                                                    'b' as blue
                                                                    'g' as green
                                                                    'r' as red
                                                                    'c' as cyan
                                                                    'm' as magenta
                                                                    'y' as yellow
                                                                    'k' as black
                                                                    'w' as white
Case-insensitive X11/CSS4 color name with no spaces.
                                                                    'aquamarine'
                                                                    'mediumseagreen'
Case-insensitive color name from xkcd color survey
with  'xkcd:'  prefix.
                                                                    'xkcd:sky blue'
                                                                    'xkcd:eggshell'
Case-insensitive Tableau Colors from 'T10' categorical palette.
 Note
This is the default color cycle.
                                                                    'tab:blue'
                                                                    'tab:orange'
                                                                    'tab:green'
                                                                    'tab:red'
                                                                    'tab:purple'
                                                                    'tab:brown'
                                                                    'tab:pink'
                                                                    'tab:gray'
                                                                    'tab:olive'
                                                                    'tab:cyan'
"CN" color spec where 'C' precedes a number acting as an index
into the default property cycle.
                                                                    'C0'
                                                                    'C1'
 Note
Matplotlib indexes color at draw time and defaults to black
if cycle does not include color.
"""
mpl.rcParams["axes.prop_cycle"]
""" these are 'tab:' colors !
(default: cycler('color', ['#1f77b4',    # 'tab:blue'
                           '#ff7f0e',    # 'tab:orange'
                           '#2ca02c',    # 'tab:green'
                           '#d62728',    # 'tab:red'
                           '#9467bd',    # 'tab:purple'
                           '#8c564b',    # 'tab:brown'
                           '#e377c2',    # 'tab:pink'
                           '#7f7f7f',    # 'tab:gray'
                           '#bcbd22',    # 'tab:olive'
                           '#17becf']))  # 'tab:cyan'
"""
#%%
"""
The two Artists combine with alpha compositing.
Matplotlib uses the equation below to compute the result of blending a new Artist.

RGB_{new} = RGB_{below} * (1 - \alpha) + RGB_{artist} * \alpha
"""
#%% "CN" color selection
"""
Matplotlib converts "CN" colors to RGBA when drawing Artists.
The `Styling with cycler`  https://matplotlib.org/stable/tutorials/intermediate/color_cycle.html
section contains additional information about controlling colors and style properties.
"""
th = np.linspace(0, 2*np.pi, 128)

def demo(style):

    mpl.style.use(style)                    #!!!

    fig, ax = plt.subplots(figsize=(3, 3))

    ax.set_title('style: {!r}'.format(style), color='C0')

    ax.plot(th, np.cos(th), 'C1', label='C1')
    ax.plot(th, np.sin(th), 'C2', label='C2')
    ax.legend()


demo('default')
demo('seaborn')

#%%
"""
The first color 'C0' is the title.
Each plot uses the second and third colors of each style's rcParams["axes.prop_cycle"]
(default:
cycler('color', ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])).
They are 'C1' and 'C2', respectively.
"""
fig = plt.figure()
ax = fig.add_subplot()

mpl.rcParams["axes.prop_cycle"]
default_cycler = ['#1f77b4',  # tab:blue
                  '#ff7f0e',  # tab:orange
                  '#2ca02c',  # tab:green
                  '#d62728',  # tab:red
                  '#9467bd',  # tab:purple (violet)
                  '#8c564b',  # tab:brown
                  '#e377c2',  # tab:pink
                  '#7f7f7f',  # tab:grey  (medium dark)
                  '#bcbd22',  # tab:olive (green-yellow-grey)
                  '#17becf']  # tab:cyan  (~teal)

for c in range(len(default_cycler)):
    ax.plot([c, c], [0, 1], color=default_cycler[c], linewidth=40)

#%%
#%% Comparison between  X11/CSS4 (~RGB) and  xkcd  colors
"""
The xkcd colors come from a user survey conducted by the webcomic xkcd.

95 out of the 148 X11/CSS4 color names also appear in the xkcd color survey.
Almost all of them map to different color values in the X11/CSS4 and in the xkcd palette.
Only 'black', 'white' and 'cyan' are identical.

For example, 'blue' maps to '#0000FF' whereas 'xkcd:blue' maps to '#0343DF'.
Due to these name collisions, all xkcd colors have the 'xkcd:' prefix.

The visual below shows name collisions.
Color names where color values agree are in bold.
"""

import matplotlib._color_data as mcd
import matplotlib.patches as mpatch

mcd.BASE_COLORS
mcd.TABLEAU_COLORS
mcd.CSS4_COLORS
mcd.XKCD_COLORS

#%%
overlap = { name for name in mcd.CSS4_COLORS
        if "xkcd:" + name in mcd.XKCD_COLORS }

fig = plt.figure(figsize=[9, 5])
ax = fig.add_axes([0, 0, 1, 1])

n_groups = 3
n_rows = len(overlap) // n_groups + 1

for j, color_name in enumerate(sorted(overlap)):
    css4 = mcd.CSS4_COLORS[color_name]
    xkcd = mcd.XKCD_COLORS["xkcd:" + color_name].upper()

    col_shift = (j // n_rows) * 3
    y_pos = j % n_rows
    text_args = dict(va='center', fontsize=10,
                     weight='bold' if css4 == xkcd else None)
    ax.add_patch(mpatch.Rectangle((0 + col_shift, y_pos), 1, 1, color=css4))
    ax.add_patch(mpatch.Rectangle((1 + col_shift, y_pos), 1, 1, color=xkcd))
    ax.text(0 + col_shift, y_pos + .5, '  ' + css4, alpha=0.5, **text_args)
    ax.text(1 + col_shift, y_pos + .5, '  ' + xkcd, alpha=0.5, **text_args)
    ax.text(2 + col_shift, y_pos + .5, '  ' + color_name, **text_args)

for g in range(n_groups):
    ax.hlines(range(n_rows), 3*g, 3*g + 2.8, color='0.7', linewidth=1)
    ax.text(0.5 + 3*g, -0.5, 'X11', ha='center', va='center')
    ax.text(1.5 + 3*g, -0.5, 'xkcd', ha='center', va='center')

ax.set_xlim(0, 3 * n_groups)
ax.set_ylim(n_rows, -1)
ax.axis('off')

plt.show()


#%%
#%%



#%%
#%%

