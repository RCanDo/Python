#! python3
"""
Usage
-----
$ py research.pyw <reg_exp> [<folder>]

Examples
--------
$ py research.pyw "^[a-z]"
$ py research.pyw ^^[a-z]
$ py research.pyw "^[A-Z !.]$"
$ py research.pyw \.$

$ py research.pyw ^^[a-z] ./sampletexts
$ py research.pyw ^^[A-Z] ./sampletexts
$ py research.pyw ^^\s+ ./sampletexts
$ py research.pyw import ./sampletexts
$ py research.pyw \.$ ./sampletexts

Remarks
-------
Use double quotes for regexp: "regexp" when it contains a raw space.
If " is not used then ^ at the beginning must be doubled.
"""

import sys, os
import re
import argparse

parser = argparse.ArgumentParser(description="Searches for lines satysfying " + \
                                             "given regular expression " + \
                                             "within files in given directory.")

parser.add_argument("regex",
                    action="store",
                    help="regular expression")

parser.add_argument(  # "-p", "--path", dest=
                    "path",
                    action="store",
                    # required=False,
                    nargs = "?",
                    default=os.getcwd(),
                    help="path to directory with files to be searched")

args = parser.parse_args()

#print(args)

reg = re.compile(args.regex.strip("\""))

files = os.listdir(args.path)
files = [f for f in files if re.search(r'\.txt$', f)]

for f in files:
    print("\t" + f)
    f = open(os.path.join(args.path, f), 'r')
    for line in f:
        # print(line.strip("\n"))
        if reg.search(line):
            print(line.strip("\n"))
        # else:
        #     print('0')
    print()
