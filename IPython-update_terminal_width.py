#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 10:16:00 2024

@author: arek

python - ipython: how to set terminal width - Stack Overflow
https://stackoverflow.com/questions/25583428/ipython-how-to-set-terminal-width
"""

import IPython
import signal
import shutil
import sys
try:
    import numpy as np
except ImportError:
    pass

c = get_config()

def update_terminal_width(*ignored):
    """Resize the IPython and numpy printing width to match the terminal."""
    w, h = shutil.get_terminal_size()

    config = IPython.get_ipython().config
    config.PlainTextFormatter.max_width = w - 1
    shell = IPython.core.interactiveshell.InteractiveShell.instance()
    shell.init_display_formatter()

    if 'numpy' in sys.modules:
        import numpy as np
        np.set_printoptions(linewidth=w - 5)

# We need to configure IPython here differently because get_ipython() does not
# yet exist.
w, h = shutil.get_terminal_size()
c.PlainTextFormatter.max_width = w - 1
if 'numpy' in sys.modules:
    import numpy as np
    np.set_printoptions(linewidth=w - 5)

signal.signal(signal.SIGWINCH, update_terminal_width)