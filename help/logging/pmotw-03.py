"""
Naming Logger Instances

All of the previous log messages all have ‘root’ embedded in them because the code uses  the root logger.
An easy way to tell where a specific log message comes from is to use a separate logger object for each module.
Log messages sent to a logger include the name of that logger.
Here is an example of how to log from different modules so it is easy to trace the source of the message.
"""
# logging_modules_example.py

import logging

logging.basicConfig(level=logging.WARNING)

logger1 = logging.getLogger('package1.module1')
logger2 = logging.getLogger('package2.module2')

logger1.warning('This message comes from one module')
logger2.warning('This comes from another module')

"""
The output shows the different module names for each output line.

$ python3 logging_modules_example.py

WARNING:package1.module1:This message comes from one module
WARNING:package2.module2:This comes from another module
"""
