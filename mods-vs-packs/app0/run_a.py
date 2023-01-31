#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROOT = .../mods-vs-packs/

1.: basic call
 ROOT $ python3 -m app0.run_a

2.: these won't work
 ROOT/app0 $ python3 -m run_a
 ROOT $ python3 app0/run_a.py

The reason is `pack0` is above "reference path" or "reference point", which is:
- cwd (current working directory) when calling `python3 -m lib.module`

- where script (file/module) which is called resides `python3 pth/to/module.py` (i.e. without -m option)

Notice that
- `library.module` ~= `library/module.py` effectively point to the same code in the same file (module).
-

"""

import sys
sys.path.insert(1, ".")     # uncomment it to see that 2. works with it (but not without)

from pathlib import Path

from pack0 import mod_a
from app0.helpers import helper_a
# this will work too
# from .helpers import helper_a

print(Path(".").absolute())

mod_a.fun_a()

helper_a()
