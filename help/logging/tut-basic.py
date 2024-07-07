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
    - title: Logging HOWTO
      link: https://docs.python.org/3.11/howto/logging.html#logging-basic-tutorial
    - title: logging — Logging facility for Python
      link: https://docs.python.org/3.11/library/logging.html
file:
    date: 2024-06-29
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""
# %%
import logging
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything

# %% Be sure to try the following in a newly started Python interpreter,
# and don’t just continue from the session described above:
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
"""
Changed in version 3.9: The `encoding` argument was added (passed to open()) ...
"""
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
