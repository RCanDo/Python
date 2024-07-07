"""
Integration with the warnings Module

The logging module integrates with warnings through captureWarnings(),
which configures warnings to send messages through the logging system instead of outputting them directly.
"""
# logging_capture_warnings.py

import logging
import warnings

logging.basicConfig(
    level=logging.INFO,
)

warnings.warn('This warning is not sent to the logs')

logging.captureWarnings(True)

warnings.warn('This warning is sent to the logs')

# %%
logger = logging.getLogger(__name__)
logging.captureWarnings(True)

warnings.warn("This warning should have better log name... but it doesn't :( ")

"""
The warning message is sent to a logger named py.warnings using the WARNING level.

$ python3 logging_capture_warnings.py

logging_capture_warnings.py:13: UserWarning: This warning is not
 sent to the logs
  warnings.warn('This warning is not sent to the logs')
WARNING:py.warnings:logging_capture_warnings.py:17: UserWarning:
 This warning is sent to the logs
  warnings.warn('This warning is sent to the logs')
"""
