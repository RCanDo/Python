#! os_summary.py
"""
work interactively!
"""

#%%
import sys
sys.path

#%%
import os

#%%
os.path.sep

os.path.join('usr','bin','spam')

#%%

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))

#%%

HOME = os.getcwd()
print(HOME)

#%%
from glob import glob
glob(HOME)
glob(os.path.join(HOME,'*'))  # all files in the folder

os.listdir(HOME)

#%%
os.chdir('C:\\Windows\\System32')
os.getcwd()
glob(os.path.join(os.getcwd(), '*'))
glob(os.path.join(os.getcwd(), '*.exe'))

#%%
os.chdir(HOME)
os.getcwd()

#%% os.makedirs()

new_directory = 'C:\\delicious\\walnut'
print(os.path.join(new_directory,'waffels'))

os.makedirs(os.path.join(new_directory,'waffels'))
glob(os.path.join(new_directory,'*'))

os.makedirs(os.path.join(new_directory,'wafers'))
glob(os.path.join(new_directory,'*'))

#%% os.rmdir(), shutil.rmtree()
os.rmdir('C:\\delicious')  # OSError: [WinError 145] The directory is not empty:

import shutil
shutil.rmtree('C:\\delicious')

glob(('C:\\delicious'))

#%%
os.chdir(new_directory)
os.chdir(HOME)

#%%
os.getcwd()

# absolute path of the argument
os.path.abspath('.')

# is argument an absolute path?
os.path.isabs('.')      # False
os.path.isabs(os.path.abspath('.'))     # True

# reletive path from the 'start' path to 'path'
os.path.relpath(path='C:\\Windows\\System32')

os.path.relpath(path=HOME, start='C:\\Windows\\System32')

#%%
os.path.dirname('C:\\Windows\\System32\\calc.exe')
os.path.basename('C:\\Windows\\System32\\calc.exe')

os.path.split('C:\\Windows\\System32\\calc.exe')


#%% size
#%%
os.path.getsize(HOME)  # size in bytes
os.listdir(HOME)

os.path.getsize('C:\\Windows\\System32\\calc.exe')

#%%
total = 0
for file in os.listdir('C:\\Windows\\System32'):
    total += os.path.getsize(os.path.join('C:\\Windows\\System32', file))
print(total/1024/1024)

#%%
os.path.exists('C:\\Windows\\System32')             # T
os.path.exists('C:\\Windows\\System32\\calc.exe')   # T
os.path.exists('C:\\Windows\\System321')            # F

#%% checking for DRIVES
os.path.exists('C:\\')
os.path.exists('D:\\')
os.path.exists('E:\\')
os.path.exists('F:\\')

#%%
os.path.isfile('C:\\Windows\\System32')             # F
os.path.isfile('C:\\Windows\\System32\\calc.exe')   # T

os.path.isdir('C:\\Windows\\System32')              # T
os.path.isdir('C:\\Windows\\System32\\calc.exe')    # F

#%% files
#%%
os.chdir(os.path.join('C:','Projects','Python','tieto2','lesson_09_reading_and_writing_files'))
## FileNotFoundError: [WinError 3] The system cannot find the path specified:
## 'C:Projects\\Python\\tieto2\\lesson_09_reading_and_writing_files'
## ???

os.chdir(os.path.join('C:\\Projects','Python','tieto2','lesson_09_reading_and_writing_files'))

os.getcwd()
os.listdir()

#%%  removing file

os.remove(path, *, dir_fd=None)
os.unlink(path, *, dir_fd=None)  ## identical!

## path must be file and cannot be directory; 
## use os.rmdir() to remove directory

#%%

baconFile = open('bacon.txt', 'w')      # opening file to write
baconFile.write('Hello World!\nHave a nice day!\n')
baconFile.close()

def printbacon():
    baconFile = open('bacon.txt')
    content = baconFile.read()
    baconFile.close()
    print(content)

printbacon()

baconFile = open('bacon.txt', 'a')      # opening file to append
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

printbacon()

def printwords():
    baconFile = open('bacon.txt')
    content = baconFile.read()
    words = content.split()
    print(words)

printwords()

#%% shelve

import shelve

shelFile = shelve.open('mydata')
cats = ['Filip', 'Filon', 'Oskar']
dogs = ['Cyryl']

shelFile['cats'] = cats
shelFile['dogs'] = dogs

shelFile.close()

#%%
os.listdir()

shelFile = shelve.open('mydata')
list(shelFile.keys())
list(shelFile.values())

del shelFile['dogs']

shelFile.close()

dd
#%%
import pprint

pets = [ dict(name='Filip', kind='cat', desc='lean'),
         dict(name='Filon', kind='cat', desc='grey'),
         dict(name='Oskar', kind='cat', desc='fluffy'),
         dict(name='Cyryl', kind='dog', desc='furry') ]
pets
pprint.pprint(pets)

pprint.pformat(pets)
print(pprint.pformat(pets))  # like a proper code

fileObj = open('myPets.py', 'w')
fileObj.write('pets = ' + pprint.pformat(pets) + '\n')
fileObj.close()

os.listdir()

import myPets
myPets.pets
myPets.pets[0]
myPets.pets[0]['kind']








