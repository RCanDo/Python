"""
02 Verbosity Levels

Another useful feature of the logging API is the ability to produce different messages at different log levels.
This means code can be instrumented with debug messages, for example,
and the log level can be set so that those debug messages are not written on a production system.
the table below lists the logging levels defined by logging.

Logging Levels
     Level 	        Value
logging.CRITICAL 	50
logging.ERROR 	    40
logging.WARNING 	30
logging.INFO 	    20
logging.DEBUG   	10
logging.NOTSET   	 0

The log message is only emitted if the `handler` and `logger` are configured
!!!    to emit messages of that level or higher.
For example, if a message is CRITICAL, and the logger is set to ERROR, the message is emitted (50 > 40).
If a message is a WARNING, and the logger is set to produce only messages set to ERROR,
the message is not emitted (30 < 40).
"""
# logging_level_example.py

import logging
import sys

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL,
}

if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical error message')

"""
Run the script with an argument like ‘debug’ or ‘warning’ to see which messages show up at different levels:

$ python3 logging_level_example.py debug

DEBUG:root:This is a debug message
INFO:root:This is an info message
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical error message

$ python3 logging_level_example.py info

INFO:root:This is an info message
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical error message
"""
