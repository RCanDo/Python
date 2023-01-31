# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os, sys, glob

#%%

ls
cd d:\roboczy\python\help\files
ls

#%%
os.chdir("D:/ROBOCZY/Python/help/files")
os.listdir()

glob.glob("./*")

#%%

with open("f0.txt", "w") as f:
    f.write(
"""
line 1
line 2
another line
yet another line
...
it never ends

[it was empty line]
ough!!
1234
    fallaout...
"""
    )

#%% writing list of txt

txt_lst = \
"""
line 1
line 2
another line
yet another line
...
it never ends

[it was empty line]
ough!!
1234
    fallaout...
""".split("\n")
txt_lst

with open("txt_from_list.txt", "w") as f:
    f.writelines(txt_lst)
# no separator between lines !!!

#%%

f = open("f0.txt", "r")
lines = f.readlines()

for l in lines:
    print(l)

f.close()

type(lines)

lines.append("")

#%%

with open("f0.txt", "r") as f:
    for l in f:
        print("{} : {}".format(f.tell()))

# OSError: telling position disabled by next() call

#%%

f = open("f0.txt", "r+")
lines = f.readlines()

any_changed = False
for k in range(len(lines)):
    l = lines[k]
    print(l, end="")
    if l.startswith("line"):
        l = l.replace("line", "lin")
        print(l)
        lines[k] = l
        any_changed = True

f.close()

f = open("f0.txt", "w")
if any_changed:
    f.writelines(lines)
f.close()


#%%
