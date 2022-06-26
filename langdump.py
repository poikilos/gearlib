#!/usr/bin/env python3
import sys
import os
import re
# import string
import hashlib

wordPattern = re.compile(r'[\W_]+')
encoding = 'utf-8'


def echo0(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


got_dict = {}


def string_to_key(sentence):
    # return hashlib.md5(s)
    # See https://stackoverflow.com/a/1277047/4541104
    # return wordPattern.sub('', sentence)
    # return re.sub(r'[\W_]+', '', sentence)
    return re.sub(r'[\W_]+', ' ', sentence, flags=re.UNICODE)
    # ^ keep ' '


def dump_value(value, prefix="data['comments']['de']['", suffix="']"):
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


def dump_values(line, sign):
    '''
    Sequential arguments:
    A line that may or may not contain multiple values, such as
    "1, y = 2" for multiple or "1" for one.
    '''
    parts = line.split(", ")
    if len(parts) == 1:
        dump_value(line)
        return
    for part in parts:
        signI = part.find(sign)
        if signI > -1:
            dump_value(part[signI+len(sign):].strip())
        else:
            dump_value(part.strip())


def dump_comments(path):
    with open(path, 'r') as ins:
        lineN = 0
        multiline = False  # in multi-line comment ("/*" to "*/")
        testValue = "Durchmesser der Mittelbohrung"
        isTest = False
        for rawL in ins:
            line = rawL.rstrip()
            isTest = False
            if testValue in line:
                isTest = True
            lineN += 1  # Counting numbers start at 1.
            multiStartI = -1
            start = 0
            keep = False
            end = len(line)
            if not multiline:
                multiStartI = line.find("/*")
                singleI = line.find("//")
                if singleI > -1:
                    if ((multiStartI < 0)
                            or (multiStartI > singleI)):
                        start = multiStartI + 2
                        dump_value(line[singleI+2:].strip())
                        continue
                if multiStartI > -1:
                    keep = True  # Always keep the first line
                    start = multiStartI + 2
                    multiline = True
            sign = " = "
            # ^ " = " comes before a variable description in Getriebe.
            if multiline:
                signI = line.find(sign)
                multiEndI = line.find("*/")
                if multiEndI > -1:
                    end = multiEndI
                    multiline = False
                if signI > -1:
                    start = signI + len(sign)
                    if (multiEndI > -1) and (signI > multiEndI):
                        # The sign is not in the comment.
                        if isTest:
                            echo0("TEST FAILED: \"{}\" result: The sign"
                                  " is not in the comment"
                                  "(signI={}, multiEndI={})."
                                  "".format(testValue, signI,
                                            multiEndI))
                            return 1
                        continue
                    value = line[start:end].strip()
                    dump_values(value, sign)
                    continue
                else:
                    echo0("Warning: The line will be ignored"
                          " since there is neither a multiline comment"
                          " opening nor '{}': {}".format(sign, line))
                # else ignore a comment that doesn't describe a variable
                # and isn't on the first line of a comment
            if isTest:
                echo0("TEST FAILED: \"{}\" result: ignore a comment"
                      " that doesn't describe a variable"
                      "".format(testValue))
                return 1
    return 0


def main():
    if len(sys.argv) < 2:
        echo0("You must specify a file in SCAD format"
              " (or another format with C-like comments).")
        return 1
    return dump_comments(sys.argv[1])


if __name__ == "__main__":
    sys.exit(main())
