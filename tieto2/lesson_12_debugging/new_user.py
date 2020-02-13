#! python3
"""
Validated user base - write script that takes email, password,
phone number and postal code, validates these fields and if validation passes,
saves it to a file as CSV with email considered as unique field.
If a record with the same email is already in the file,
the old record should be altered by new one.
Use validators implemented in lesson 8, exercises 2, 3, 4 and 5.

As part of this exercise write combined_validator function that takes email,
password, phone number and postal code and throws exceptions
if any of arguments doesn't pass validation. Add 'verbose output'.
"""

import sys, os
import argparse, logging
import re

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

DESCRIPTION = """
Takes email, password phone number and postal code, 
validates these fields and if validation passes, 
saves it to a file as CSV with email considered as unique field. 
If a record with the same email is already in the file, 
the old record is altered by new one.
"""

parser = argparse.ArgumentParser(description=DESCRIPTION)

parser.add_argument("-e", "--email", dest="email",
                    action="store",
                    required=True,
                    help="user e-mail -- used as unique user ID")

parser.add_argument("-p", "--password", dest="pwd",
                    action="store",
                    required=True,
                    help="user password")

parser.add_argument("-n", "--phone_number", dest="phone",
                    action="store",
                    default="",
                    required=False,
                    help="user phone number")

parser.add_argument("-z", "--zip", dest="zip",
                    action="store",
                    default="",
                    required=False,
                    help="user postal code (zip)")

parser.add_argument("-v", "--verbosity", dest="verb",
                    action="count",
                    default=0,
                    required=False,
                    help="verbosity of output")

parser.add_argument("-o", "--output", dest="output",
                    action="store",
                    default="user_base.csv",
                    help="output file")

args = parser.parse_args()

if args.verb == 0:
    logging.disable(logging.CRITICAL)
elif args.verb == 1:
    logging.disable(logging.DEBUG)
else:
    pass


# validatiors
# -----------

def validate_email(email):

    if not re.match(r'.{5,254}', email):
        raise Exception('e-mail address cannot exceed 254 characters and '
                        'cannot be shorter then 5.')

    regex = re.compile(r'^(\w+[.-])*(\w+)@(\w+[.-])*(\w+)\.(\w+)$',
                       re.IGNORECASE)

    if not regex.match(email):
        raise Exception('We do not accept e-mails of this form, sorry! :(')

    return True


def validate_password(password):

    if not re.search(r'^.{8,}$', password):
        raise Exception('Password must have at least 8 characters.')

    if not re.search(r'[a-z]', password):
        raise Exception('Password must have at least 1 lowercase letter.')

    if not re.search(r'[A-Z]', password):
        raise Exception('Password must have at least 1 UPPERcase letter.')

    if not re.search(r'\d', password):
        raise Exception('Password must have at least 1 digit.')

    return True


def validate_phone(phone):

    regex = re.compile(r'^((\+|00)\d{2} )?(\d{3}[- ]){2}(\d{3})$')

    if not regex.match(phone):
        raise Exception("This is not valid phone number.")

    return True


def validate_zip(zip):

    regex = re.compile(r'^\d{2}-\d{3}')

    if not regex.match(zip):
        raise Exception("Polish postal code is of the format DD-DDD where "
                        "each D is a separate digit.")

    return True


# validation and new record
# -------------------------

validate_email(args.email)
validate_password(args.pwd)
if args.phone != "":
    validate_phone(args.phone)
if args.zip != "":
    validate_zip(args.zip)


args_dict = dict(args._get_kwargs())
logging.debug("%s" % str(args_dict))

record_new = ",".join([args_dict[key]
                       for key in ["email", "pwd", "phone", "zip"]])
logging.debug("new record: {}".format(str(record_new)))


# update or append
# ----------------
# simple solution - rewriting whole file - good for small files
# rewriting one line within a file needs additional package (fileinput ?)

file = open(args.output, 'r')
lines = file.readlines()

# is user already present?

email_found = False
for k in range(len(lines)):
    if lines[k].startswith(args.email + ","):
        logging.debug("old record: {}".format(lines[k]))
        lines[k] = record_new + "\n"
        email_found = True
        break

file.close()


# update or append:

if email_found:
    logging.info("entry for user  %s  will be updated" % args.email)
    with open(args.output, 'w') as file:
        file.writelines(lines)
else:
    logging.info("entry for user  %s  will be appended" % args.email)
    with open(args.output, 'a') as file:
        file.write(record_new + "\n")
