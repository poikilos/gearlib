#!/usr/bin/env python3
from __future__ import print_function
import sys

verbose = 0
for argI in range(1, len(sys.argv)):
    arg = sys.argv[argI]
    if arg.startswith("--"):
        if arg == "--verbose":
            verbose = 1
        elif arg == "--debug":
            verbose = 2


def is_verbose():
    return verbose > 0


def write0(arg):
    sys.stderr.write(arg)
    sys.stderr.flush()


def write1(arg):
    if verbose < 1:
        return
    sys.stderr.write(arg)
    sys.stderr.flush()


def write2(arg):
    if verbose < 2:
        return
    sys.stderr.write(arg)
    sys.stderr.flush()


def echo0(*args, **kwargs):  # formerly prerr
    print(*args, file=sys.stderr, **kwargs)


def echo1(*args, **kwargs):  # formerly debug
    if verbose < 1:
        return
    print(*args, file=sys.stderr, **kwargs)


def echo2(*args, **kwargs):  # formerly extra
    if verbose < 2:
        return
    print(*args, file=sys.stderr, **kwargs)
