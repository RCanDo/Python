#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
title: tempfile — Temporary File System Objects
type: tutorial
keywords: []
description: |
    Create temporary file system objects.
todo:
remarks:
sources:
    - title: tempfile — Temporary File System Objects
      link: https://pymotw.com/3/tempfile/index.html
      description: |
file:
    date: 2023-07-15
    authors:
        - email: akasp@int.pl
"""
# %%
import os
import tempfile
import pathlib

# %%
print('Building a filename with PID:')
filename = '/tmp/guess_my_name.{}.txt'.format(os.getpid())
with open(filename, 'w+b') as temp:
    print('temp:')
    print('  {!r}'.format(temp))
    print('temp.name:')
    print('  {!r}'.format(temp.name))

# Clean up the temporary file yourself.
os.listdir("/tmp")      # ...,  'guess_my_name.265493.txt',  ...
os.remove(filename)

# %%
# The file returned by TemporaryFile() has no name.
print('TemporaryFile:')
with tempfile.TemporaryFile() as temp:
    print('temp:')
    print('  {!r}'.format(temp))
    print('temp.name:')
    print('  {!r}'.format(temp.name))

# Automatically cleans up the file.

# %%
"""
By default, the file handle is created with mode 'w+b' so it behaves consistently on all platforms
and the caller can write to it and read from it.
"""

with tempfile.TemporaryFile() as temp:
    temp.write(b'Some data')

    temp.seek(0)
    print(temp.read())

# %%
# To open the file in text mode, set mode to 'w+t' when the file is created.

with tempfile.TemporaryFile(mode='w+t') as f:
    f.writelines(['first\n', 'second\n'])

    f.seek(0)
    for line in f:
        print(line.rstrip())

# %% Named Files
"""
There are situations where having a named temporary file is important.
For applications spanning multiple processes, or even hosts,
naming the file is the simplest way to pass it between parts of the application.
The NamedTemporaryFile() function creates a file without unlinking it, so it retains its name
(accessed with the name attribute).

The file is removed after the handle is closed.
"""

with tempfile.NamedTemporaryFile() as f:
    print('temp:')
    print('  {!r}'.format(f))
    print('temp.name:')
    print('  {!r}'.format(f.name))

    f = pathlib.Path(f.name)

print('Exists after close:', f.exists())
f
f.with_suffix(".qq")

# %% Spooled Files
"""
For temporary files containing relatively small amounts of data,
it is likely to be more efficient to use a  SpooledTemporaryFile
because it holds the file contents in memory using
 io.BytesIO  or  io.StringIO  buffer
until they reach a threshold size.

When the amount of data passes the threshold,
it is “rolled over” and written to disk,
and then the buffer is replaced with a normal TemporaryFile().

This example uses private attributes of the SpooledTemporaryFile
to determine when the  rollover to disk  has happened.
It is not normally necessary to check this status except when tuning the buffer size.
"""

with tempfile.SpooledTemporaryFile(
        max_size=100,
        mode='w+t',
        encoding='utf-8'
) as t:
    print('temp: {!r}'.format(t))

    for i in range(4):
        print(i)
        t.write('\nThis line is repeated over and over.')
        print(t._rolled, t._file)

# %%
"""
To explicitly cause the buffer to be written to disk,
call the  rollover()  or  fileno()  methods.

In this example, because the buffer size is so much larger than the amount of data,
no file would be created on disk except that rollover() was called.
"""

with tempfile.SpooledTemporaryFile(
        max_size=1000,
        mode='w+t',
        encoding='utf-8'
) as t:
    print('temp: {!r}'.format(t))

    for i in range(3):
        print(i)
        t.write('This line is repeated over and over.\n')
        print(t._rolled, t._file)
    print('rolling over')
    t.rollover()
    print(t._rolled, t._file)

# %% Temporary Directories
"""
When several temporary files are needed,
it may be more convenient to create a single temporary directory with
 TemporaryDirectory
and open all of the files in that directory.

The context manager produces the name of the directory,
which can then be used within the context block to build other file names.
"""

with tempfile.TemporaryDirectory() as d:
    p = pathlib.Path(d)
    print(p)
    f = p / 'f.txt'
    print(f)
    f.write_text('This file is deleted.')

print('Directory exists after?', p.exists())
print('Contents after:', list(p.glob('*')))

# %% Predicting Names
"""
While less secure than strictly anonymous temporary files,
including a predictable portion in the name
makes it possible to find the file and examine it for debugging purposes.
All of the functions described so far take three arguments to control the filenames to some degree.
Names are generated using the formula:

    dir / prefix + random + suffix

All of the values except random
can be passed as arguments to the functions for creating temporary files or directories.

The prefix and suffix arguments are combined with a random string of characters to build the filename,
and the dir argument is taken as-is and used as the location of the new file.
"""

with tempfile.NamedTemporaryFile(
        suffix='_suffix',
        prefix='prefix_',
        dir='/tmp'
) as t:
    print('temp:')
    print('  ', t)
    print('temp.name:')
    print('  ', t.name)

"""
temp:
   <tempfile._TemporaryFileWrapper object at 0x7f072c2fc6d0>
temp.name:
   /tmp/prefix_001wgipe_suffix
"""

# %% Temporary File Location
"""
If an explicit destination is not given using the dir argument,
the path used for the temporary files will vary based on the current platform and settings.

The tempfile module includes two functions for querying the settings being used at runtime.
"""

print('gettempdir():', tempfile.gettempdir())
print('gettempprefix():', tempfile.gettempprefix())

"""
gettempdir() returns the default directory that will hold all of the temporary files and
gettempprefix() returns the string prefix for new file and directory names.

The value returned by gettempdir() is set based
on a straightforward algorithm of looking through a list of locations
for the first place the current process can create a file.
The search list is:

1. The environment variable TMPDIR
2. The environment variable TEMP
3. The environment variable TMP
4. A fallback, based on the platform.
   Windows uses the first available of C:\temp, C:\tmp, \temp, or \tmp.
   Other platforms use /tmp, /var/tmp, or /usr/tmp.
5. If no other directory can be found, the current working directory is used.

Programs that need to use a global location for all temporary files
without using any of these environment variables
should set  tempfile.tempdir  directly by assigning a value to the variable.

"""
dir(tempfile)

# %%
