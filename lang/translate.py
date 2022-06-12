#!/usr/bin/env python3
from __future__ import print_function
import os
import sys
import re
import json
from de import load_lang as load_lang_de
from en import load_lang as load_lang_en

myPath = os.path.abspath(__file__)
myDir = os.path.dirname(myPath)
repoDir = os.path.dirname(myDir)

verbose = 0


def echo0(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def echo1(*args, **kwargs):
    if verbose < 1:
        return
    print(*args, file=sys.stderr, **kwargs)


roots = ['comments', 'variables', 'parameters', 'param_help',
         'functions']
functions_start_flag = "// Global"


def generate_skel(data, doc_opener_keys, lang):
    if data.get('comments') is None:
        data['comments'] = {}
    for root in roots:
        if data.get(root) is None:
            data[root] = {}
        if data[root].get(lang) is None:
            data[root][lang] = {}
    if doc_opener_keys.get(lang) is None:
        doc_opener_keys[lang] = {}


def replace_whole_word(oldStr, newStr, haystack):
    '''
    Get haystack but with oldStr replaced with newStr only where each
    match is a whole word.
    '''
    # Regex notes:
    # "\\b" (literally `\b`) means word break (opposite of "W")
    # re.search(r"\b" + re.escape(oldStr) + r"\b", haystack)
    return re.sub(r"\b" + re.escape(oldStr) + r"\b", newStr, haystack)


def keysByLongestValue(d):
    '''
    Sort starting where the value is longest, but only return the keys.
    '''
    tuples = list(d.items())  # Create a list of (key, value) tuples.
    tuples.sort(key=lambda x: len(x[1]), reverse=True)
    echo1("ORDER:")
    for t in tuples:
        echo1(t)
    return [x[0] for x in tuples]


param_help_doc = ("Each param_help key must have two parts such as"
                  " \"rack module\"")
known_decls = ["function", "module"]
doc_opener_doc = ("The value of doc_opener_keys must start with a"
                  " declaration of a known type (any of {} followed by"
                  " a name)"
                  "".format(known_decls))


def uncommented_stripped(line):
    line = line.strip()
    if line.startswith("//"):
        line = line[2:]
    elif line.startswith("/*"):
        line = line[2:]
    if line.endswith("*/"):
        line = line[:-2]
    line = line.strip()
    return line


def rewrite_as_lang(srcPath, dstPath, data, doc_opener_keys,
                    fromLang, toLang, tab="    "):
    '''
    Sequential arguments:
    doc_opener_keys -- If the function with the name (in data)
        referenced by the key in here didn't occur yet, don't assume
        arguments are correct for it. For example, if
        doc_opener_keys[lang]['rack'] == 'module rack tip',
        the value of data['comments'][lang]['module rack tip'] must
        occur before variable documentation is translated such as
        data['parameters'][lang]['rack length'].
        - It must be the whole line excluding "/*" or "*/"
    '''
    documenting_func = None
    lines = []
    with open(srcPath, 'r') as ins:
        for rawL in ins:
            line = rawL.rstrip()
            lines.append(line)
    replacements = {}
    keys = []
    for categoryName, category in data.items():
        for sourceKey, source in category[fromLang].items():
            keys.append(source)
            # replacements[source] =
    started_funcs = False
    combined = {}
    for root_key, langs in data.items():
        for lang, d in langs.items():
            combined[lang] = {}
            for key, pattern in d.items():
                if combined[lang].get(key) is not None:
                    raise ValueError(
                        "{} already exists for {}".format(key, lang)
                    )
                combined[lang][key] = pattern
    orderedKeys = keysByLongestValue(combined[fromLang])
    # ^ This is useful for doing the longest first (If context consideration
    #   isn't implemented, longest first is the only way to correctly identify
    #   terms).
    with open(dstPath, 'w') as outs:
        lineN = 0
        documenting_func = None
        doc_closing = None
        for line in lines:
            lineN += 1
            sys.stderr.write("\r")
            sys.stderr.write("* processing line {} of {}...            "
                             "".format(lineN, len(lines)))
            if documenting_func is None:
                for function, dKey in doc_opener_keys[fromLang].items():
                    if not started_funcs:
                        break
                    tryFlag = data['comments'][fromLang][dKey]
                    if tryFlag == uncommented_stripped(line):
                        documenting_func = function
                        declParts = dKey.split(" ")
                        if declParts[0] not in known_decls:
                            raise ValueError("{} but the value was {}"
                                             "".format(doc_opener_doc,
                                                       dKey))
                        declType = declParts[0]
                        doc_closing = ("{} {}("
                                       "".format(declType, function))
                        echo0("* documenting {} until \"{}\""
                              "".format(documenting_func, doc_closing))
                        break
                    else:
                        pass
                        '''
                        echo0("[debug] {} is not in: \"{}\""
                              "".format(tryFlag, line))
                        '''
            orderedCommentsKeys = keysByLongestValue(data['comments'][fromLang])
            # echo0("dict order test:")
            # for strKey, fromStr in data['comments'][fromLang].items():
            for strKey in orderedCommentsKeys:
                fromStr = data['comments'][fromLang][strKey]
                # echo0("  {}: \"{}\"".format(strKey, fromStr))
                toStr = data['comments'][toLang][strKey]
                line = line.replace(fromStr, toStr)

            orderedParamKeys = keysByLongestValue(data['param_help'][fromLang])
            # for strKey, fromStr in data['param_help'][fromLang].items():
            for strKey in orderedParamKeys:
                fromStr = data['param_help'][fromLang][strKey]
                toStr = data['param_help'][toLang][strKey]
                strKeyParts = strKey.split(" ")
                strKeyFunction = None
                '''
                if strKeyParts[0] != "function":
                    raise ValueError("Each param_help key must start"
                                     " with \"function\", but the key"
                                     " is \"{}\"".format(strKey))
                '''
                if len(strKeyParts) != 2:
                    raise ValueError("{}, but the key"
                                     " is \"{}\""
                                     "".format(param_help_doc, strKey))
                strKeyFunction = strKeyParts[0]
                if strKeyFunction == documenting_func:
                    line = line.replace(fromStr, toStr)

            for strKey, fromStr in data['parameters'][fromLang].items():
                toStr = data['parameters'][toLang][strKey]
                line = replace_whole_word(fromStr, toStr, line)
            for strKey, fromStr in data['variables'][fromLang].items():
                toStr = data['variables'][toLang][strKey]
                line = replace_whole_word(fromStr, toStr, line)
            for strKey, fromStr in data['functions'][fromLang].items():
                toStr = data['functions'][toLang][strKey]
                line = replace_whole_word(fromStr, toStr, line)
            outs.write("{}\n".format(line))
            line = line.replace("\t", tab)
            if documenting_func is not None:
                if doc_closing in line:
                    doc_closing = None
                    documenting_func = None
                else:
                    echo0("  * documenting {} with: {}"
                          "".format(documenting_func, line))
            # end for line
            if functions_start_flag in line:
                started_funcs = True

        sys.stderr.write("\r")
        sys.stderr.write("* processing line {} of {}...OK              "
                         "".format(lineN, len(lines)))
        echo0("")


def main():
    data = {}
    doc_opener_keys = {}
    '''
    if len(sys.argv) < 3:
        echo0("Error: You must specify a source and destination file.")
        exit(1)
    srcPath = sys.argv[1]
    dstPath = sys.argv[2]
    '''
    srcPath = os.path.realpath(os.path.join(repoDir, "Getriebe.scad"))
    dstPath = os.path.realpath(os.path.join(repoDir, "gearlib.scad"))
    if not os.path.isfile(srcPath):
        echo0("Error: {} doesn't exist.".format(json.dumps(srcPath)))
        return 1
    generate_skel(data, doc_opener_keys, 'de')
    load_lang_de(data, doc_opener_keys)
    generate_skel(data, doc_opener_keys, 'en')
    load_lang_en(data, doc_opener_keys)
    echo0("* writing \"{}\"...".format(dstPath))
    rewrite_as_lang(srcPath, dstPath, data, doc_opener_keys,
                    'de', 'en')
    return 0


if __name__ == "__main__":
    sys.exit(main())
