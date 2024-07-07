#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
title: fstring tricks
source:
    - link: https://www.youtube.com/watch?v=EoNOWVYKyo0
    - link: https://www.youtube.com/watch?v=aa39jL7wdJs
file:
    date: 2024-03-17
"""
# %%  1.

n: int = 1000000000
f"{n}"      # '1000000000'
f"{n:_}"    # '1_000_000_000'
f"{n:,}"    # '1,000,000,000'
# no other separators possible

n: int = 1_000_000_000
f"{n}"      # '1000000000'

# %%
x: float = 1234.5678
f"{x}"              # '1234.5678'
f"{round(x, 2)}"    # '1234.57'
f"{x:.2f}"          # '1234.57'
f"{x:.2}"           # '1.2e+03'
f"{x:,.2f}"         # '1,234.57'

# number format as variable
float_format = ',.2f'
f"{x:float_format}"     #! ValueError: Invalid format specifier
# nesting {} works:
f"{x:{float_format}}"   # '1,234.57'

# %%  :e  on integers
n: int = 1_620_000_000
f"{n:e}"    # '1.620000e+09'
f"{n:.2e}"  # '1.62e+09'
f"{n:.2}"   #! ValueError: Precision not allowed in integer format specifier

# %%  2.
v: str = 'var'
'1234567890' # '1234567890'
f"{v:>10}"   # '       var'
f"{v:>10}:"  # '       var:'
f"{v:<10}:"  # 'var       :'    default, i.e. no need for '<'
f"{v:10}:"   # 'var       :'
f"{v:^10}:"  # '   var    :'    centering

# with filling
f"{v:_>10}:" # '_______var:'
f"{v:.<10}:" # 'var.......:'
f"{v:-^10}:" # '---var----:'

# %%
f"{x:>10_.2f}"

# %%  3.
import datetime as dt

now = dt.datetime.now()
now         # datetime.datetime(2024, 3, 17, 11, 36, 27, 594025)
f"{now}"    # '2024-03-17 11:36:27.594025'
f"{now:%y.%m.%d}"  # '24.03.17'
f"{now:%y%m%d}"    # '240317'
f"{now:%y%m%d-%H%M%S}"    # '240317-113627'

f"{now:%c}"     # 'nie, 17 mar 2024, 11:36:27'     local version (formatting?) of datetime
f"{now:%I}"     #  11      ?
f"{now:%p}"     #          ?  am/pm ?

# datetime format as variable
dt_spec = '%y%m%d-%H%M%S'
f"{now:dt_spec}"    #! 'dt_spec'  -- NO!
# nesting {} works
f"{now:{dt_spec}}"  # '240317-113627'  OK!

# %%  debugging code with fstring
a = 2
b = 3
s = "Qq ryq!"

f"a + b = {a + b}"      # 'a + b = 5'   may be shortened to:
f"{a + b = }"           # 'a + b = 5'   GREAT !!!
f"a + b = {a + b = }"   # !  'a + b = a + b = 5' – doppelt gemoppelt :P – don't do this !!!

f"{bool(a) = }"         # 'bool(a) = True'

f"{s = }"               # "s = 'Qq ryq!'"
f"{s = !s}"             # 's = Qq ryq!'         !s – use `s` as string
f"{s = !r}"             # "s = 'Qq ryq!'"       !s – use `s` representation (default)

# %%
a = .1
b = .2
f"{a + b = }"       # 'a + b = 0.30000000000000004'
f"{a + b = :.2}"    # 'a + b = 0.3'
f"{a + b = :.2f}"   # 'a + b = 0.30'
f"{a + b = :.1f}"    # 'a + b = 0.3'
f"{a + b = :.1}"    # 'a + b = 0.3'

# %%
