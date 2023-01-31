#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 10:49:12 2022

@author: arek
"""

#%%
import io
#dir(io)

# Write a string to a buffer
output = io.StringIO()

_ = output.write('Python Exercises, Practice, Solution')
# Retrieve the value written
print("---" , output.getvalue())
# Discard buffer memory
output.close()


#%%
# see also:
# https://stackoverflow.com/questions/1218933/can-i-redirect-the-stdout-into-some-sort-of-string-buffer
import io
from contextlib import redirect_stdout

with io.StringIO() as buf, redirect_stdout(buf):
    print('redirected 0')
    print('redirected 1')
    output = buf.getvalue()

for l in output.split("\n")[:-1]:
    print("---", l)


#%%
#%%
txt = \
"""
abc
 def
ghij
   klmn
0 1 2
"""

#%%
#%% IF
buf = io.StringIO()
_ = buf.writelines(txt)
# then only
print(buf.getvalue())
# works

print(buf.read())   #! nothing
print(buf.readlines())   # []   #! nothing

#%% because
buf = io.StringIO()
_ = buf.writelines(txt)
buf.tell()  # 29
# pointer set at the end
buf.seek(0)
buf.tell()  # 0
print(buf.readlines())   # ['\n', 'abc\n', ' def\n', 'ghij\n', '   klmn\n', '0 1 2\n']   #! nothing
buf.tell()  # 29
buf.seek(0)
print(buf.read())
# OK

#%%
#%% IF
buf = io.StringIO(txt)
buf.tell()      # 0
# then
print(buf.getvalue())
# works

# also
for l in buf.readlines():
    print("---", l, end="")
# and
print(buf.read())
# works
#!!! but like iterator -- only once

print(buf.readline())    # ??? always nothing !!!

#%% i.e.
"""
 io.StringIO(txt)
does not move pointer to the end of 'file'
while
 buf = io.StringIO()
 _ = buf.write(txt)
moves the pointer to the end

Moreover

 buf.getvalue()
always reads the whole content
while
 buf.read() / buf.readlines()
moves pointer to the end
"""


#%%
#%%
buf = io.StringIO()
_ = buf.writelines(txt)

for l in buf.readlines():
    print("---", l)

# nothing ... :(

#%%
buf = io.StringIO()
_ = buf.write(txt)

for l in buf.readlines():
    print("---", l)
# nothing ... :(

#%%  this is good
buf = io.StringIO(txt)
for l in buf.readlines():
    print("---", l, end="")

#! works !!!

#%%  this is good too
buf = io.StringIO(txt)
print(buf.read())
#! works !!!
# but no way of appending sth for each line

#%%
buf = io.StringIO()
_ = buf.writelines(txt)

with open(buf, 'tr') as b:
    for l in b.readlines():
        print(l)

#! TypeError: expected str, bytes or os.PathLike object, not _io.StringIO

#%%
buf = io.StringIO()
_ = buf.writelines(txt)

print(buf.read())

# nothing

#%%
"""
!!! so what the .read() or .readlines() is for ???
"""
#%%
buf = io.StringIO()
_ = buf.writelines(txt)

print(buf.getvalue())
# OK !

#%%
buf = io.StringIO()
_ = buf.write(txt)
print(buf.getvalue())
# OK ! the same result

#%%
buf = io.StringIO(txt)
print(buf.getvalue())
# OK

#%%
buf = io.StringIO()
_ = buf.write(txt)

print(buf.read())

#%%
buf.tell()
buf.getvalue()
print(buf.read())
buf.seek(0)
