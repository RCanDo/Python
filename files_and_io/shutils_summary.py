#! shutil_summary.py
"""
work interactively!
"""

import shutil, os

#%% copying

os.chdir('C:\\')

shutils.copy('C:\\spam.txt', 'C:\\delicious')

shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')

shutil.copytree('C:\\bacon', 'C:\\bacon_backup')

#%% moving

shutil.move('C:\\bacon.txt', 'C:\\eggs')

shutil.move('spam.txt', 'c:\\does_not_exist\\eggs\\ham')  # ERROR

#%% deleting - permanently !!!

os.unlink('path')
os.rmdir('path')   # only empty folders
os.rmtree('path')

for filename in os.listdir():
    if filename.endswith('.rxt'):
        #os.unlink(filename)        # be carefull
        print(filename)             # run it first to see what you are to delete

#%% it's better to send to system Trash

# install 3d party send2trash
# $ pip install send2trash

import send2trash

baconFile = open('bacon.txt', 'a') # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')

# Note that the send2trash() function can only send files to the recycle bin; it cannot pull files out of it.

#%% Walking a Directory Tree

import os

for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')

#%%
#%% Compressing Files with the zipfile Module

import zipfile, os

os.chdir('C:\\')    # move to the folder with example.zip

#%% Reading ZIP Files

exampleZip = zipfile.ZipFile('example.zip')  # creating ZipFile object (like with open('file'))

exampleZip.namelist()
# ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']

spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
spamInfo.compress_size
'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2))
# 'Compressed file is 3.63x smaller!'

exampleZip.close()

#%% Extracting from ZIP Files

exampleZip = zipfile.ZipFile('example.zip')

exampleZip.extractall()                  # to current folder
exampleZip.extractall('C:\\ delicious')  # to the given folder

exampleZip.close()

#%% Creating and Adding to ZIP Files

newZip = zipfile.ZipFile('new.zip', 'w')  # erases the content of a file (if exists)
newZip = zipfile.ZipFile('new.zip', 'a')  # append mode == adds content

newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)

newZip.close()

#%%
