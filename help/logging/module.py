import logging

logger = logging.getLogger(__name__)    # name of a file is passed

def fun(a=1):
    logger.info(f"I'm a module.fun({a}).")
