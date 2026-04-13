#!/usr/bin/env python3

import sys

# Silent Pipe Patch: redirect all normal print() outputs to stderr
# if we are streaming the video output to stdout.
if '--stream-output' in sys.argv:
    sys.stdout = sys.stderr

# Import the tkinter fix to patch the ScreenChanged error
import tkinter_fix

from modules import core

if __name__ == '__main__':
    core.run()
