#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Scatter plots with a legend
subtitle:
version: 1.0
type: tutorial
keywords: [legend, scatter plot]
description: |
remarks:
todo:
sources:
    - title: Scatter plots with a legend
      link: https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html
    - title:
      link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: ex-01-scatter_plot_with_legend.py
    path: E:/ROBOCZY/Python/graphics/matplotlib/legend/
    date: 2021-10-27
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""





#%%
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
#plt.style.use('fast')
# see `plt.style.available` for list of available styles

#%%  Scatter plots with a legend
"""
To create a scatter plot with a legend one may use a LOOP
and create one scatter plot per item
to appear in the legend and set the label accordingly.

The following also demonstrates how transparency of the markers can be adjusted
by giving alpha a value between 0 and 1.
"""
np.random.seed(19680801)

fig, ax = plt.subplots()
for color in ['tab:blue', 'tab:orange', 'tab:green']:
    n = 100
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()

#%% Automated legend creation   !!!
"""
Another option for creating a legend for a scatter is to use the
    `PathCollection.legend_elements()` method.
It will automatically try to determine a useful number of legend entries
to be shown and return a tuple of handles and labels.
Those can be passed to the call to legend.
"""
N = 45
x, y = np.random.rand(2, N)               # 2 x N ~ U(0, 1)
c = np.random.randint(1, 5, size=N)       # 5 random colors
s = np.random.randint(10, 220, size=N)    # many random sizes

fig, ax = plt.subplots()

scatter = ax.scatter(x, y, c=c, s=s)

# produce a legend with the unique colors from the scatter
legend_color = ax.legend( *scatter.legend_elements(),
    loc="lower left",
    title="Classes")

ax.add_artist(legend_color)     #!!!  necessary            -- because only last legend is displayed "automaticaly"

# produce a legend with a cross section of sizes from the scatter
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6, color='gray')

legend_size = ax.legend( handles, labels,
    loc="upper right",
    title="Sizes")
# ax.add_artist(legend_size)    # not necessary    ???      -- the last does not need it   -- !?!?!?! really!!!

plt.show()

#%% closer look
scatter    # matplotlib.collections.PathCollection
vars(scatter)       #! it's big; may be huge
dir(scatter)        # ... legend_elements ...

help(scatter.legend_elements)
"""
legend_elements(prop='colors',
                num='auto',
                fmt=None,
                func=<function PathCollection.<lambda> at 0x0000017B1FDF58B0>,
                **kwargs)
    method of matplotlib.collections.PathCollection instance
Create `legend handles` and `labels` for a `PathCollection`.

Each legend handle is a `.Line2D` representing the `Path` that was drawn,
and each label is a string what each `Path` represents.

This is useful for obtaining a legend for a `~.Axes.scatter` plot;
e.g.:

    scatter = plt.scatter([1, 2, 3],  [4, 5, 6],  c=[0, 5, 10])
    plt.legend(*scatter.legend_elements())

creates three legend elements, one for each color with the numerical
values passed to `c` as the labels.

Also see the `automatedlegendcreation` example.

Parameters
----------
prop : {"colors", "sizes"}, default: "colors"
    If "colors", the legend handles will show the different colors of
    the collection. If "sizes", the legend will show the different
    sizes. To set both, use *kwargs* to directly edit the `.Line2D`
    properties.
num : int, None, "auto" (default), array-like, or `~.ticker.Locator`
    Target number of elements to create.
    If None, use all unique elements of the mappable array. If an
    integer, target to use *num* elements in the normed range.
    If *"auto"*, try to determine which option better suits the nature
    of the data.
    The number of created elements may slightly deviate from *num* due
    to a `~.ticker.Locator` being used to find useful locations.
    If a list or array, use exactly those elements for the legend.
    Finally, a `~.ticker.Locator` can be provided.
fmt : str, `~matplotlib.ticker.Formatter`, or None (default)
    The format or formatter to use for the labels. If a string must be
    a valid input for a `~.StrMethodFormatter`. If None (the default),
    use a `~.ScalarFormatter`.
func : function, default: ``lambda x: x``
    Function to calculate the labels.  Often the size (or color)
    argument to `~.Axes.scatter` will have been pre-processed by the
    user using a function ``s = f(x)`` to make the markers visible;
    e.g. ``size = np.log10(x)``.  Providing the inverse of this
    function here allows that pre-processing to be inverted, so that
    the legend labels have the correct values; e.g. ``func = lambda
    x: 10**x``.
**kwargs
    Allowed keyword arguments are *color* and *size*. E.g. it may be
    useful to set the color of the markers if *prop="sizes"* is used;
    similarly to set the size of the markers if *prop="colors"* is
    used. Any further parameters are passed onto the `.Line2D`
    instance. This may be useful to e.g. specify a different
    *markeredgecolor* or *alpha* for the legend handles.

Returns
-------
handles : list of `.Line2D`
    Visual representation of each element of the legend.
labels : list of str
    The string labels for elements of the legend.   -- LaTeX !!!
"""
scatter.legend_elements()
scatter.legend_elements('sizes')

#%%
#%%
"""
Further arguments to the  `PathCollection.legend_elements()`  method
can be used to steer how many legend entries are to be created
and how they should be labeled.
The following shows how to use some of them.
"""
np.random.seed(987)
volume = np.random.rayleigh(27, size=40)
amount = np.random.poisson(10, size=40)
ranking = np.random.normal(size=40)
price = np.random.uniform(1, 10, size=40)

fig, ax = plt.subplots()

# Because the price is much too small when being provided as size for `s`,
# we normalize it to some useful point sizes,
#   s = .3 * (price * 3)**2
scatter = ax.scatter(volume, amount, c=ranking, s=0.3*(price*3)**2,
                     vmin=-3, vmax=3,  #!!!
                     cmap="cool")

# Produce a legend for the ranking (colors).
# Even though there are 40 different rankings,
# we only want to show 5 of them in the legend.
legend_rank = ax.legend( *scatter.legend_elements(num=6),
    loc="upper left",
    title="Ranking")

ax.add_artist(legend_rank)

#%%  Produce a legend for the price (sizes).
# Because we want to show the prices in dollars,
# we use the `func` argument to supply the inverse of the function
# used to calculate the sizes from above.
# The `fmt` ensures to show the price in dollars.
# Note how we target at 5 elements here, but obtain only 4 in the
# created legend due to the automatic round prices that are chosen for us.

kw = dict(
    prop = "sizes",
    num = 5,
    color = scatter.cmap(0.5),
    fmt = "$ {x:.2f}",
    func = lambda s: np.sqrt(s/.3)/3
    )

legend_price = ax.legend( *scatter.legend_elements(**kw),
    loc="lower right",
    title="Price")

plt.show()


#%%