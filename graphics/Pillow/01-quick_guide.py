#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begins with ---

title: Pillow Quick Guide
subtitle:
version: 1.0
type: module
keywords: [PyTorch, NN, AI]   # there are always some keywords!
description: |
remarks:
    - my version of v1
todo:
sources:
    - title: PIL homepage
      link: https://pillow.readthedocs.io/en/latest/index.html
    - title: Pillow Quick Guide
      link: https://www.tutorialspoint.com/python_pillow/python_pillow_quick_guide.htm
    - title: Pillow Concepts
      link: https://pillow.readthedocs.io/en/latest/handbook/concepts.html#modes
file:
    usage:
        interactive: True
        terminal: True
    name: 03-data.py
    path: ~/Projects/AIML/NNRL/PyTorch
    date: 2022-03-16
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
              - arek@staart.pl
"""

#%%
from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

path_data = Path("/home/arek/Data/pictures/")
#path_data = Path("/home/arek/QuantUp/FU/fu-qu/data/meshcnn1/test/image/")

#%% Open image using Image module
im = Image.open(path_data / "P1280422.JPG")
#im = Image.open(path_data / "shrec__1_0_r270,-150,0.png")
#Show actual Image
im.show()

#%% Show rotated Image
im45 = im.rotate(45)
im45.show()

#%%
plt.imshow(im)

plt.figure(2)
plt.imshow(im45)

#%%
# im    #! pictire displayed in a console... :)
dir(im)
im.filename
im.format
im.size     # (3648, 2736)
im.width
im.height
im.info     # ooops... -- non-readable and very long

#%% !!! mode !!!
# https://pillow.readthedocs.io/en/latest/handbook/concepts.html#modes
im.mode     # 'RGB'
im.getbands()   # ('R', 'G', 'B')
im.palette  # None

# !!! The palette mode ('P') uses a color palette to define the actual color for each pixel.
# hence there is no palette for modes other then 'P'.

#%% convert()   https://pillow.readthedocs.io/en/latest/reference/Image.html#PIL.Image.Image.convert
help(im.convert)
imrgba = im.convert("RGBA")
imrgba

imrgba_np = np.array(imrgba)
imrgba_np.shape     # (96, 96, 4)

#%%
#imrgb = im.convert("RGB")
#imrgb.getbands()

#%% saving (to other formats)
im.save('szp2016.jpg')
im.save('szp2016.bmp')

#%% thumbnails
"""
 Image.thumbnail(size, resample=3)
size − Required size
resample − Optional resampling filter.
    It can be one of these
    PIL.Image.NEAREST,
    PIL.Image.BILINEAR,
    PIL.Image.BICUBIC, or
    PIL.Image.LANCZOS.
    If omitted, it defaults to PIL.Image.BICUBIC.
Returns None.
"""
im.thumbnail((90,90))   #
plt.imshow(im)
im.size   # (90, 68)  !!!  no-larger then given size with proportions retained

im.save('szp2016_thumb.jpg')
imt = Image.open('szp2016_thumb.jpg')

im = Image.open(im_path)

#%% ,thumbnail() works in-place and there is no functional version... :(
imt = im.thumbnail((90, 100))
imt  # None
im.size

# use .copy()
im = Image.open(im_path)
imt = im.copy()
imt.thumbnail((90, 90))
im.size    # (3648, 2736)
imt.size   # (90, 68)

#%%
iml = im.convert('L')
iml.mode   # 'L'

f1 = plt.figure(1)
plt.imshow(iml)
f1.clear()
plt.imshow(iml, cmap="binary")

f2 = plt.figure(2)
plt.imshow(iml, cmap="Greys")
## very little difference

## both are NEGATIVES !
## How to get the BW version of color image ???

#%% Layers
"""
 Image.merge(mode, bands)
mode − The mode to use for the output image.
bands − A sequence containing one single-band image for each band in the output image.
    All bands must have the same size.
Return value − An Image objects.
"""
r, g, b = im.split()
r.mode   # 'L'
fig, ax = plt.subplots(1, 3, figsize=(15,5), num=3, tight_layout=True)
ax[0].imshow(r, cmap='Greys')
ax[1].imshow(g, cmap='Greys')
ax[2].imshow(b, cmap='Greys')

#%%
fig, ax = plt.subplots(1, 3, figsize=(15,5), num=4, tight_layout=True)
ax[0].imshow(r, cmap='binary')
ax[1].imshow(g, cmap='binary')
ax[2].imshow(b, cmap='binary')

# no difference
# both are negatives !

#%% Merging Images

im2_path = Path(path_data / "P1280795.JPG")

#Read the two images
im = Image.open(im_path)
im2 = Image.open(im2_path)

plt.figure(5)
plt.imshow(im2)

#!!!  RESIZE  !!!
im2 = im2.resize(im.size)

new_image = Image.new('RGB', (2*im.size[0], im.size[1]), (250,250,250))
new_image.paste(im, (0,0))
new_image.paste(im2, (im.size[0], 0))
new_image.save("merged_images.jpg")

plt.figure(6)
plt.imshow(new_image)

#%%
#%% Crop
cropped = im2.crop((500, 500, 2500, 1500))
plt.figure(7)
plt.imshow(cropped)


#%% M L with Numpy
#%% Creating image from Numpy Array
"""
Creating an RGB image using PIL and save it as a jpg file.
In the following example we will −
 Create a 150 by 250-pixel array.
 Fill left half of the array with orange.
 Fill right half of the array with blue.
"""
import numpy as np

arr = np.zeros([150, 250, 3], dtype=np.uint8)
arr[:,:100] = [255, 128, 0]
arr[:,100:] = [0, 0, 255]

img = Image.fromarray(arr)

f1 = plt.figure(1)
plt.imshow(img)

#%% Creating greyscale images
"""
Creating greyscale images is slightly different from creating an RGB image.
We can use the 2-dimensional array to create a greyscale image.
"""
import numpy as np
arr = np.zeros([150,300], dtype=np.uint8)

#Set grey value to black or white depending on x position
for x in range(300):
   for y in range(150):
      if (x % 16) // 8 == (y % 16) // 8:
         arr[y, x] = 0
      else:
         arr[y, x] = 255

img = Image.fromarray(arr)
img.mode    # 'L'

plt.close("all")

plt.figure(1)
plt.imshow(img)

plt.figure(2)
plt.imshow(img, cmap="binary")

#%% Creating numpy array from an Image
img2arr = np.array(cropped)
img2arr
img2arr.shape   # (1000, 2000, 3)

# going back again
plt.imshow(Image.fromarray(img2arr))



#%%
#%% Flip and Rotate
"""
We are going to use the transpose (method) function from the Image module for flipping the images.
Some of the mostly commonly used methods supported by ‘transpose()’ are −
 Image.FLIP_LEFT_RIGHT − For flipping the image horizontally
 Image.FLIP_TOP_BOTTOM − For flipping the image vertically
 Image.ROTATE_90       − For rotating the image by specifying degree
"""
# Example 1: Horizontally flipped Image
ax[0].imshow(cropped.transpose(Image.FLIP_LEFT_RIGHT))
ax[1].imshow(cropped.transpose(Image.FLIP_TOP_BOTTOM))
ax[2].imshow(cropped.transpose(Image.ROTATE_90))

#%% Adding Filters
from PIL import ImageFilter
"""
ImageFilter.BLUR
    .CONTOUR
    .DETAIL
    .EDGE_ENHANCE
    .EDGE_ENHANCE_MORE
    .EMBOSS
    .FIND_EDGES
    .SHARPEN
    .SMOOTH
    .SMOOTH_MORE
"""
ax[0].imshow(cropped.filter(ImageFilter.BLUR))
ax[1].imshow(cropped.filter(ImageFilter.MinFilter(3)))
ax[2].imshow(cropped.filter(ImageFilter.MinFilter))      # the same as MiniFiler(3)

#%% Colors on an Image
...

#%% Blur
...

#%% Creating a Watermark
...

#%% ImageDraw Module
...

#%% Image Sequences
# animations  like .gif
...

#%% Writing Text
...
