# https://docs.python.org/3.6/howto/logging.html#logging-basic-tutorial

import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

####
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')


#### second handler
# create console handler and set level to debug
ch2 = logging.StreamHandler()
ch2.setLevel(logging.WARNING)

# create formatter
formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch2.setFormatter(formatter2)

# add ch to logger
logger.addHandler(ch2)

""" !!! Notice that the message below is doubled !!! 
"""
# 'application' code
logger.debug('debug message 2')
logger.info('info message 2')
logger.warning('warning message 2')
logger.error('error message 2')
logger.critical('critical message 2')
""" This is because it 'belongs' to both Handlers: `ch` and `ch2`.
"""
