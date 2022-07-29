#!/usr/bin/env python3
from __future__ import print_function
import os
import sys
import platform

HOME = None
if platform.system() == "Windows":
    HOME = os.environ['USERPROFILE']
else:
    HOME = os.environ['HOME']

TRY_G_REPO = os.path.join(HOME, "git", "getriebe")
if os.path.isdir(TRY_G_REPO):
    sys.path.insert(0, TRY_G_REPO)
else:
    print("* There is no {}. Trying regular import..."
          "".format(TRY_G_REPO), file=sys.stderr)

from pyopenscad import (
    echo0,
    echo1,
    echo2,
)

tryLexRepo = os.path.join(HOME, "Downloads", "git",
                          "bath_open_instrumentation_group", "sca2d")
if os.path.isdir(tryLexRepo):
    sys.path.insert(0, tryLexRepo)
else:
    echo0("* There is no {}. Trying regular import..."
          "".format(tryLexRepo))

try:
    import sca2d
except ModuleNotFoundError as ex:
    if "No module named 'lark'" in str(ex):
        echo0("You must install sca2d properly.")
    else:
        raise ex

submoduleDir = os.path.dirname(os.path.abspath(__file__))
moduleDir = os.path.dirname(submoduleDir)
repoDir = os.path.dirname(moduleDir)

in_scad_name = "Getriebe.scad"
in_scad = os.path.join(repoDir, in_scad_name)

if not os.path.isfile(in_scad):
    raise FileNotFoundError(in_scad)

# region from sca2d/sca2d/setup.py
entry_points = {'console_scripts': ['sca2d = sca2d.__main__:main']}
# endregion from sca2d/sca2d/setup.py
from sca2d.__main__ import main as sca2d_main

def main():
    sys.argv = ['sca2d', in_scad]
    return(sca2d_main())
    return 0

if __name__ == "__main__":
    sys.exit(main())
