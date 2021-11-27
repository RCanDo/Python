# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 09:01:40 2021

@author: staar
"""

#%%
import matplotlib as mpl
help(mpl.figure) # too big -- this is sub-module !
dir(mpl.figure)

help(mpl.figure.Figure)  # it's still big!

#%% see first simpler pyplot constructor

import matplotlib.pyplot as plt
help(plt.figure)

#%%
"""
figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True,
       FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)

    Create a new figure, or activate an existing figure.

    Parameters
    ----------
    num : int or str, optional
        A unique identifier for the figure.

        If a figure with that identifier already exists, this figure is made
        active and returned.
        An integer refers to the ``Figure.number``
        attribute, a string refers to the figure label.

        If there is no figure with the identifier or *num* is not given, a new
        figure is created, made active and returned.
        If *num* is an int, it
        will be used for the ``Figure.number`` attribute, otherwise, an
        auto-generated integer value is used (starting at 1 and incremented
        for each new figure). If *num* is a string, the figure label and the
        window title is set to this value.

    figsize : (float, float), default: :rc:`figure.figsize`
        Width, height in inches.

    dpi : float, default: :rc:`figure.dpi`
        The resolution of the figure in dots-per-inch.

    facecolor : color, default: :rc:`figure.facecolor`
        The background color.

    edgecolor : color, default: :rc:`figure.edgecolor`
        The border color.

    frameon : bool, default: True
        If False, suppress drawing the figure frame.

    FigureClass : subclass of `~matplotlib.figure.Figure`
        Optionally use a custom `.Figure` instance.

    clear : bool, default: False
        If True and the figure already exists, then it is cleared.

    tight_layout : bool or dict, default: :rc:`figure.autolayout`
        If ``False`` use *subplotpars*. If ``True`` adjust subplot
        parameters using `.tight_layout` with default padding.
        When providing a dict containing the keys ``pad``, ``w_pad``,
        ``h_pad``, and ``rect``, the default `.tight_layout` paddings
        will be overridden.

    constrained_layout : bool, default: :rc:`figure.constrained_layout.use`
        If ``True`` use constrained layout to adjust positioning of plot
        elements.  Like ``tight_layout``, but designed to be more
        flexible.  See
        :doc:`/tutorials/intermediate/constrainedlayout_guide`
        for examples.  (Note: does not work with `add_subplot` or
        `~.pyplot.subplot2grid`.)


    **kwargs : optional
        See `~.matplotlib.figure.Figure` for other possible arguments.

    Returns
    -------
    `~matplotlib.figure.Figure`
        The `.Figure` instance returned will also be passed to
        new_figure_manager in the backends, which allows to hook custom
        `.Figure` classes into the pyplot interface. Additional kwargs will be
        passed to the `.Figure` init function.

    Notes
    -----
    If you are creating many figures, make sure you explicitly call
    `.pyplot.close` on the figures you are not using, because this will
    enable pyplot to properly clean up the memory.

    `~matplotlib.rcParams` defines the default values, which can be modified
    in the matplotlibrc file.
"""
#%%

plt.figure(1, clear=True)  # clearing figure 1 (if exists)
plt.figure(1, tight_layout=True)

#%%
fig = mpl.figure.Figure()
ax = fig.add_subplot()
ax.plot(range(5), [3, 2, 5, 4, 1])
# nothing...

fig.draw(...)     # ???

fig.show()  # AttributeError: Figure.show works only for figures managed by pyplot,
            # normally created by pyplot.figure()

#%%
#%%
import matplotlib as mpl
help(mpl.figure) # too big -- this is sub-module !
dir(mpl.figure)

help(mpl.figure.Figure)

# https://matplotlib.org/stable/api/figure_api.html#module-matplotlib.figure
"""
Parameters:

figsize : 2-tuple of floats, default: rcParams["figure.figsize"] (default: [6.4, 4.8])
    Figure dimension (width, height) in inches.

dpi : float, default: rcParams["figure.dpi"] (default: 100.0)
    Dots per inch.

facecolor : default: rcParams["figure.facecolor"] (default: 'white')
    The figure patch facecolor.

edgecolor : default: rcParams["figure.edgecolor"] (default: 'white')
    The figure patch edge color.

linewidth : float
    The linewidth of the frame (i.e. the edge linewidth of the figure patch).

frameonbool : default: rcParams["figure.frameon"] (default: True)
    If False, suppress drawing the figure background patch.

subplotpars : SubplotParams
    Subplot parameters. If not given, the default subplot parameters rcParams["figure.subplot.*"] are used.

tight_layout : bool or dict, default: rcParams["figure.autolayout"] (default: False)
    If False use subplotpars.
    If True adjust subplot parameters using tight_layout with default padding.
    When providing a dict containing the keys pad, w_pad, h_pad, and rect,
    the default tight_layout paddings will be overridden.

constrained_layout : bool, default: rcParams["figure.constrained_layout.use"] (default: False)
    If True use constrained layout to adjust positioning of plot elements.
    Like tight_layout, but designed to be more flexible. See Constrained Layout Guide for examples. (Note: does not work with add_subplot or subplot2grid.)

"""
#%%
