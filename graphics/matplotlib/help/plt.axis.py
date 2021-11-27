# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 09:56:09 2021

@author: staar
"""
#%%
import matplotlib as mpl
import matplotlib.pyplot as plt

help(plt.axis)

#%%
"""
axis(*args, emit=True, **kwargs)
    Convenience method to get or set some axis properties.

Call signatures::

  xmin, xmax, ymin, ymax = axis()
  xmin, xmax, ymin, ymax = axis([xmin, xmax, ymin, ymax])
  xmin, xmax, ymin, ymax = axis(option)
  xmin, xmax, ymin, ymax = axis(**kwargs)

Parameters
----------
xmin, xmax, ymin, ymax : float, optional
    The axis limits to be set.  This can also be achieved using ::

        ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))

option : bool or str
    If a bool, turns axis lines and labels on or off.
    If a string, possible values are:

    ======== ==========================================================
    Value    Description
    ======== ==========================================================
    'on'     Turn on axis lines and labels. Same as ``True``.
    'off'    Turn off axis lines and labels. Same as ``False``.
    'equal'  Set equal scaling (i.e., make circles circular) by
             changing axis limits. This is the same as
             ``ax.set_aspect('equal', adjustable='datalim')``.
             Explicit data limits may not be respected in this case.
    'scaled' Set equal scaling (i.e., make circles circular) by
             changing dimensions of the plot box. This is the same as
             ``ax.set_aspect('equal', adjustable='box', anchor='C')``.
             Additionally, further autoscaling will be disabled.
    'tight'  Set limits just large enough to show all data, then
             disable further autoscaling.
    'auto'   Automatic scaling (fill plot box with data).
    'image'  'scaled' with axis limits equal to data limits.
    'square' Square plot; similar to 'scaled', but initially forcing
             ``xmax-xmin == ymax-ymin``.
    ======== ==========================================================

emit : bool, default: True
    Whether observers are notified of the axis limit change.
    This option is passed on to `~.Axes.set_xlim` and
    `~.Axes.set_ylim`.

Returns
-------
xmin, xmax, ymin, ymax : float
    The axis limits.

See Also
--------
matplotlib.axes.Axes.set_xlim
matplotlib.axes.Axes.set_ylim
"""

#%%
import numpy as np

#%%  scale & grid
N = 10
y = np.zeros(N)

plt.semilogx(np.geomspace(1, 1000, N, endpoint=True), y + 1, 'o')
plt.semilogx(np.geomspace(1, 1000, N, endpoint=False), y + 2, 'o')

plt.axis([0.5, 2000, 0, 3])
plt.grid(True, color='0.7', linestyle='-', which='both', axis='both')

#%%
zzu = np.geomspace(-1+0j, 1+0j, num=22)  # Circle
zzd = np.geomspace(1+0j, -1+0j, num=22)  # Circle

plt.plot(np.r_[zzd.real, zzd.real], np.r_[zzd.imag, -zzd.imag])
plt.axis('scaled')

#%%
xx, yy = np.meshgrid([-1, 0, 1], [-2, 0, 2])
xx
yy

plt.scatter(xx, yy)
plt.plot(np.r_[zzd.real, zzd.real], np.r_[zzd.imag, -zzd.imag])
plt.axis('square')
plt.axis('equal')
plt.axis('scaled')
plt.axis('tight')
plt.axis('auto')
plt.axis('image')

#%% OO style (via ax.method())
# more complicated

fig, ax = plt.subplots()
ax.scatter(xx, yy)
ax.plot(np.r_[zzd.real, zzd.real], np.r_[zzd.imag, -zzd.imag])
ax.set_aspect('square')     #! ValueError: could not convert string to float: 'square'
ax.set_aspect('equal')
ax.set_aspect('scaled')     #! ValueError: could not convert string to float: 'scaled'
ax.set_aspect('tight')      #! ValueError: could not convert string to float: 'tight'
ax.set_aspect('auto')
ax.set_aspect('image')      #! ValueError: could not convert string to float: 'image'

ax.set(xlim=(-2, 2), ylim=(-2, 2))

#%%
help(ax.set_aspect)
help(ax.set_adjustable)
help(ax.set_anchor)

ax.set_adjustable('box')
ax.set_adjustable('datalim')
