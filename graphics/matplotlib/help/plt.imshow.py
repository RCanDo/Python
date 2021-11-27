# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:16:07 2021

@author: staar
"""
#%%
import matplotlib as mpl
import matplotlib.pyplot as plt


#%%
fig, ax = plt.subplots()
help(ax.imshow)
# or just
help(plt.imshow)
#%%
"""

Help on method imshow in module matplotlib.axes._axes:

imshow(`X`, cmap=None, norm=None, aspect=None, interpolation=None,
       alpha=None, vmin=None, vmax=None, origin=None, extent=None,
       *,
       filternorm=True, filterrad=4.0, resample=None, url=None, data=None,
       **kwargs)

method of matplotlib.axes._subplots.AxesSubplot instance

Display data as an image, i.e., on a 2D regular raster.

The input may either be actual RGB(A) data, or 2D scalar data, which
will be rendered as a pseudocolor image.

For displaying a __grayscale__
image set up the colormapping using the parameters
   `cmap='gray', vmin=0, vmax=255`.

The number of pixels used to render an image is set by the Axes size
and the *dpi* of the figure.
This can lead to aliasing artifacts when
the image is resampled because the displayed image size will usually
not match the size of *X*
(see  `/gallery/images_contours_and_fields/image_antialiasing`).
The resampling can be controlled via the
   `interpolation`  parameter and/or  `image.interpolation`.

Parameters
----------
    X : array-like or PIL image
        The image data. Supported array shapes are:

        - (M, N): an image with scalar data. The values are mapped to
          colors using normalization and a colormap. See parameters *norm*,
          *cmap*, *vmin*, *vmax*.
        - (M, N, 3): an image with RGB values (0-1 float or 0-255 int).
        - (M, N, 4): an image with RGBA values (0-1 float or 0-255 int),
          i.e. including transparency.

        The first two dimensions (M, N) define the rows and columns of
        the image.

        Out-of-range RGB(A) values are clipped.

    cmap : str or `~matplotlib.colors.Colormap`, default: :rc:`image.cmap`
        The Colormap instance or registered colormap name used to map
        scalar data to colors. This parameter is ignored for RGB(A) data.

    norm : `~matplotlib.colors.Normalize`, optional
        The `.Normalize` instance used to scale scalar data to the [0, 1]
        range before mapping to colors using *cmap*. By default, a linear
        scaling mapping the lowest value to 0 and the highest to 1 is used.
        This parameter is ignored for RGB(A) data.

    aspect : {'equal', 'auto'} or float, default: :rc:`image.aspect`
        The aspect ratio of the Axes.  This parameter is particularly
        relevant for images since it determines whether data pixels are
        square.

        This parameter is a shortcut for explicitly calling
        `.Axes.set_aspect`. See there for further details.

        - 'equal': Ensures an aspect ratio of 1. Pixels will be square
          (unless pixel sizes are explicitly made non-square in data
          coordinates using *extent*).
        - 'auto': The Axes is kept fixed and the aspect is adjusted so
          that the data fit in the Axes. In general, this will result in
          non-square pixels.

    interpolation : str, default: :rc:`image.interpolation`
        The interpolation method used.

        Supported values are 'none', 'antialiased', 'nearest', 'bilinear',
        'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite',
        'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell',
        'sinc', 'lanczos', 'blackman'.

        If *interpolation* is 'none', then no interpolation is performed
        on the Agg, ps, pdf and svg backends. Other backends will fall back
        to 'nearest'. Note that most SVG renderers perform interpolation at
        rendering and that the default interpolation method they implement
        may differ.

        If *interpolation* is the default 'antialiased', then 'nearest'
        interpolation is used if the image is upsampled by more than a
        factor of three (i.e. the number of display pixels is at least
        three times the size of the data array).  If the upsampling rate is
        smaller than 3, or the image is downsampled, then 'hanning'
        interpolation is used to act as an anti-aliasing filter, unless the
        image happens to be upsampled by exactly a factor of two or one.

        See
        :doc:`/gallery/images_contours_and_fields/interpolation_methods`
        for an overview of the supported interpolation methods, and
        :doc:`/gallery/images_contours_and_fields/image_antialiasing` for
        a discussion of image antialiasing.

        Some interpolation methods require an additional radius parameter,
        which can be set by *filterrad*. Additionally, the antigrain image
        resize filter is controlled by the parameter *filternorm*.

    alpha : float or array-like, optional
        The alpha blending value, between 0 (transparent) and 1 (opaque).
        If *alpha* is an array, the alpha blending values are applied pixel
        by pixel, and *alpha* must have the same shape as *X*.

    vmin, vmax : float, optional
        When using scalar data and no explicit *norm*, *vmin* and *vmax*
        define the data range that the colormap covers. By default,
        the colormap covers the complete value range of the supplied
        data. It is deprecated to use *vmin*/*vmax* when *norm* is given.
        When using RGB(A) data, parameters *vmin*/*vmax* are ignored.

    origin : {'upper', 'lower'}, default: :rc:`image.origin`
        Place the [0, 0] index of the array in the upper left or lower
        left corner of the Axes. The convention (the default) 'upper' is
        typically used for matrices and images.

        Note that the vertical axis points upward for 'lower'
        but downward for 'upper'.

        See the :doc:`/tutorials/intermediate/imshow_extent` tutorial for
        examples and a more detailed description.

    extent : floats (left, right, bottom, top), optional
        The bounding box in data coordinates that the image will fill.
        The image is stretched individually along x and y to fill the box.

        The default extent is determined by the following conditions.
        Pixels have unit size in data coordinates. Their centers are on
        integer coordinates, and their center coordinates range from 0 to
        columns-1 horizontally and from 0 to rows-1 vertically.

        Note that the direction of the vertical axis and thus the default
        values for top and bottom depend on *origin*:

        - For ``origin == 'upper'`` the default is
          ``(-0.5, numcols-0.5, numrows-0.5, -0.5)``.
        - For ``origin == 'lower'`` the default is
          ``(-0.5, numcols-0.5, -0.5, numrows-0.5)``.

        See the :doc:`/tutorials/intermediate/imshow_extent` tutorial for
        examples and a more detailed description.

    filternorm : bool, default: True
        A parameter for the antigrain image resize filter (see the
        antigrain documentation).  If *filternorm* is set, the filter
        normalizes integer values and corrects the rounding errors. It
        doesn't do anything with the source floating point values, it
        corrects only integers according to the rule of 1.0 which means
        that any sum of pixel weights must be equal to 1.0.  So, the
        filter function must produce a graph of the proper shape.

    filterrad : float > 0, default: 4.0
        The filter radius for filters that have a radius parameter, i.e.
        when interpolation is one of: 'sinc', 'lanczos' or 'blackman'.

    resample : bool, default: :rc:`image.resample`
        When *True*, use a full resampling method.  When *False*, only
        resample when the output image is larger than the input image.

    url : str, optional
        Set the url of the created `.AxesImage`. See `.Artist.set_url`.

    Returns
    -------
    `~matplotlib.image.AxesImage`

    Other Parameters
    ----------------
    **kwargs : `~matplotlib.artist.Artist` properties
        These parameters are passed on to the constructor of the
        `.AxesImage` artist.

    See Also
    --------
    matshow : Plot a matrix or an array as an image.

    Notes
    -----
    Unless *extent* is used, pixel centers will be located at integer
    coordinates. In other words: the origin will coincide with the center
    of pixel (0, 0).

    There are two common representations for RGB images with an alpha
    channel:

    -   Straight (unassociated) alpha: R, G, and B channels represent the
        color of the pixel, disregarding its opacity.
    -   Premultiplied (associated) alpha: R, G, and B channels represent
        the color of the pixel, adjusted for its opacity by multiplication.

    `~matplotlib.pyplot.imshow` expects RGB images adopting the straight
    (unassociated) alpha representation.

    .. note::
        In addition to the above described arguments, this function can take
        a *data* keyword argument. If such a *data* argument is given,
        every other argument can also be string ``s``, which is
        interpreted as ``data[s]`` (unless this raises an exception).

        Objects passed as **data** must support it
"""

#%%
#%%