#!/usr/bin/env python3
from __future__ import print_function
import sys

verbosity = 0
done_args = []
for argI in range(1, len(sys.argv)):
    arg = sys.argv[argI]
    if arg == "--verbose":
        done_args.append(arg)
        if "--debug" in done_args:
            continue
        verbosity = 1
    elif arg == "--debug":
        done_args.append(arg)
        verbosity = 2

got_dict = {}


def get_verbosity():
    return verbosity


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


def string_to_key(sentence):
    # return hashlib.md5(s)
    # See https://stackoverflow.com/a/1277047/4541104
    # return wordPattern.sub('', sentence)
    # return re.sub(r'[\W_]+', '', sentence)
    return re.sub(r'[\W_]+', ' ', sentence, flags=re.UNICODE)
    # ^ keep ' '


def emit_py_value(value, prefix="data['comments']['de']['", suffix="']"):
    key = string_to_key(value)
    if len(key) == 0:
        echo0("Warning: \"{}\" has no alphanumeric characters"
              "and will get a hash id".format(value))
        sBytes = value.encode(encoding)
        key = hashlib.md5(sBytes)
    key = key.replace("'", '\\\'')
    if key in got_dict:
        echo0("# already got ['{}'] = \"{}\"".format(key, value))
        return
    got_dict[key] = value
    print('{}{}{} = "{}"'
          ''.format(prefix, key, suffix, value.replace("\"", "\\\"")))


def emit_py_values(line, sign):
    '''
    Sequential arguments:
    A line that may or may not contain multiple values, such as
    "1, y = 2" for multiple or "1" for one.
    '''
    parts = line.split(", ")
    if len(parts) == 1:
        emit_py_value(line)
        return
    for part in parts:
        signI = part.find(sign)
        if signI > -1:
            emit_py_value(part[signI+len(sign):].strip())
        else:
            emit_py_value(part.strip())
