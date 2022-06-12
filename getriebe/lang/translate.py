#!/usr/bin/env python3
from __future__ import print_function
import os
import sys
import platform

profile = None

tryLexRepo = os.path.join(profile, "Downloads", "git", "bath_open_instrumentation_group", "sca2d")
if os.path.isfile(tryLexRepo):
    sys.path.insert(0, tryLexRepo)

import sca2d

# region from sca2d/sca2d/setup.py
entry_points = {'console_scripts': ['sca2d = sca2d.__main__:main']}
# endregion from sca2d/sca2d/setup.py
from sca2d.__main__ import sca2d_main

def main():
    pass

if __name__ == "__main__":
    main()
