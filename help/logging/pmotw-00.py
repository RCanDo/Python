# python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Logging
subtitle:
version: 1.0
type: tutorial
keywords: [logging]
description: |
remarks:
    - etc.
todo:
    - problem 1
sources:
    - title: Python Module Of The Week
      chapter: logging — Report Status, Error, and Informational Messages
      link: https://pymotw.com/3/logging/
    - title: logging — Logging facility for Python
      link: https://docs.python.org/3.11/library/logging.html
file:
    date: 2024-06-28
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
# import utils.ak as ak
# import utils.builtin as bi

# %%
"""
Purpose:	Report status, error, and informational messages.

The logging module defines a standard API for reporting errors and status information from applications and libraries.
The key benefit of having the logging API provided by a standard library module is that all Python modules
can participate in logging, so an application’s log can include messages from third-party modules.

Logging Components

The logging system is made up of four interacting types of objects.
Each module or application that wants to log uses a `Logger` instance to add information to the logs.
Invoking the logger creates a `LogRecord`, which is used to hold the information in memory until it is processed.
A `Logger` may have a number of `Handler` objects configured to receive and process log records.
The `Handler` uses a `Formatter` to turn the log records into output messages.

Logging in Applications vs. Libraries

Application developers and library authors can both use logging,
but each audience has different considerations to keep in mind.

Application developers configure the logging module, directing the messages to appropriate output channels.
It is possible to log messages with different verbosity levels or to different destinations.
`Handler`s for writing log messages to files, HTTP GET/POST locations, email via SMTP, generic sockets,
or OS-specific logging mechanisms are all included,
and it is possible to create  custom log destination classes  for special requirements
not handled by any of the built-in classes.

Developers of libraries can also use logging and have even less work to do.
Simply create a logger instance for each context, using an appropriate name,
and then log messages using the  standard levels.
As long as a library uses the logging API with consistent naming and level selections,
the application can be configured to show or hide messages from the library, as desired.
"""

# %% Logging to a File
"""
Most applications are configured to log to a file.
Use the `basicConfig()` function to set up the default handler so that debug messages are written to a file.
"""
# logging_file_example.py

import logging

LOG_FILENAME = 'logging_example.out'

logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)

logging.debug('This message should go to the log file')

with open(LOG_FILENAME, 'rt') as f:
    body = f.read()

print('FILE:')
print(body)


# %% The Logging Tree
""" !!! (some pictures here)
https://pymotw.com/3/logging/#the-logging-tree
"""
