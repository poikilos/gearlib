#!/usr/bin/env python3

from pyopenscad import (
    dump_value,
    dump_values,
)


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
