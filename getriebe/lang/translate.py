#!/usr/bin/env python3
from __future__ import print_function
import os
import sys
import platform

profile = None
if platform.system() == "Windows":
    profile = os.environ['USERPROFILE']
else:
    profile = os.environ['HOME']

tryGetriebeRepo = os.path.join(profile, "git", "getriebe")
if os.path.isdir(tryGetriebeRepo):
    sys.path.insert(0, tryGetriebeRepo)
else:
    print("* There is no {}. Trying regular import..."
          "".format(tryGetriebeRepo), file=sys.stderr)

from getriebe import (
    echo0,
    echo1,
    echo2,
)

tryLexRepo = os.path.join(profile, "Downloads", "git", "bath_open_instrumentation_group", "sca2d")
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
