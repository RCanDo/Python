# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:24:44 2019

@author: kasprark
"""



#%%

"""
https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python

Print a string that starts a color/style, then the string,
then end the color/style change with '\x1b[0m':
"""

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

print_format_table()

#%%

print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')

#%%
#%%

x = 0
for i in range(24):
  colors = ""
  for j in range(5):
    code = str(x+j)
    colors = colors + "\33[" + code + "m\\33[" + code + "m\033[0m "
  print(colors)
  x=x+5
  
#%%
#%%
  
CSI="\x1B["
print(CSI+"31;40m" + "Colored Text" + CSI + "0m")  
print(CSI+"31;40m" + u"\u2588" + CSI + "0m")
