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
import logging
from argparse import Namespace

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


parser = argparse.ArgumentParser(description="Searches for lines satisfying " + \
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

parser.add_argument("-v", "--verbosity", dest="verbosity",
                    action="count",
                    default=0,
                    help="verbosity of output"
                    )

args = parser.parse_args()

if args.verbosity == 0:
    logging.disable(logging.CRITICAL)
elif args.verbosity == 1:
    logging.disable(logging.DEBUG)
else:
    pass

logging.debug('args = %s' % args)

reg = re.compile(args.regex.strip("\""))

try:
    files = os.listdir(args.path)
    logging.info('files = %s' % files)
except FileNotFoundError as msg:
    logging.warning(msg)  # 'path %s not found' % args.path)

try:
    files = [f for f in files if re.search(r'\.txt$', f)]
    logging.info('files = %s' % files)
except NameError as msg:
    logging.error(msg)  # 'files = %s' % files)
    sys.exit(1)

for f in files:
    print("\t" + f)
    try:
        f = open(os.path.join(args.path, f), 'r')
    except FileNotFoundError as msg:
        logging.error("%s - that's impossible!" % msg)

    for line in f:
        if reg.search(line):
            print(line.strip("\n"))
        else:
            logging.info("0")
    print()
