#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 09:26:43 2022

@author: arek
"""
from pathlib import Path
from sss.bb import bb

if __name__ == "__main__":
    print(Path(".").absolute())     # working dir (not where file resides)
    print(Path(__file__))           # where file resides WITH file name
    print(Path(__file__).parent)    # where file resides without file name
    print(Path(__file__).parent.absolute())     # " but absolute path

    aa = Path("../../aa")
    path = Path(__file__).parent.absolute() / aa
    print(path)

    print(list(path.parents))

    print(bb())
