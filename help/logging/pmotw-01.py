"""
01 Rotating Log Files

Running the script repeatedly causes more messages to be appended to the file.
To create a new file each time the program runs, pass a filemode argument to basicConfig() with a value of 'w'.
Rather than managing the creation of files this way, though, it is better to use a RotatingFileHandler,
which creates new files automatically and preserves the old log file at the same time.
"""
# logging_rotatingfile_example.py

import glob
import logging
import logging.handlers

LOG_FILENAME = 'logging_rotatingfile_example.out'

# Set up a specific logger with our desired output level
logger = logging.getLogger('MyLogger')
logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME,
    maxBytes=20,
    backupCount=5,
)
logger.addHandler(handler)

# Log some messages
for i in range(20):
    logger.debug('i = %d' % i)

# See what files are created
logfiles = glob.glob('%s*' % LOG_FILENAME)
for filename in sorted(logfiles):
    print(filename)

"""
The result is six separate files, each with part of the log history for the application.

$ python3 logging_rotatingfile_example.py

logging_rotatingfile_example.out
logging_rotatingfile_example.out.1
logging_rotatingfile_example.out.2
logging_rotatingfile_example.out.3
logging_rotatingfile_example.out.4
logging_rotatingfile_example.out.5

The most current file is always logging_rotatingfile_example.out,
and each time it reaches the size limit it is renamed with the suffix .1.
Each of the existing backup files is renamed to increment the suffix (.1 becomes .2, etc.) and the .5 file is erased.

Note
Obviously, this example sets the log length much too small as an extreme example.
Set maxBytes to a more appropriate value in a real program.
"""
