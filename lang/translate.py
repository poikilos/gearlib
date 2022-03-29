#!/usr/bin/env python3
import os
import sys
import re
from de import load_lang as load_lang_de
from en import load_lang as load_lang_en

myPath = os.path.abspath(__file__)
myDir = os.path.dirname(myPath)
repoDir = os.path.dirname(myDir)


def error(*args, **kwargs):
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
                        error("* documenting {} until \"{}\""
                              "".format(documenting_func, doc_closing))
                        break
                    else:
                        pass
                        '''
                        error("[debug] {} is not in: \"{}\""
                              "".format(tryFlag, line))
                        '''
            orderedKeys = keysByLongestValue(data['comments'][fromLang])
            # error("dict order test:")
            for strKey in orderedKeys:
            # for strKey, fromStr in data['comments'][fromLang].items():
                fromStr = data['comments'][fromLang][strKey]
                # error("  {}: \"{}\"".format(strKey, fromStr))
                toStr = data['comments'][toLang][strKey]
                line = line.replace(fromStr, toStr)
            for strKey, fromStr in data['param_help'][fromLang].items():
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
                    error("  * documenting {} with: {}"
                          "".format(documenting_func, line))
            # end for line
            if functions_start_flag in line:
                started_funcs = True

        sys.stderr.write("\r")
        sys.stderr.write("* processing line {} of {}...OK              "
                         "".format(lineN, len(lines)))
        error("")

def main():
    data = {}
    doc_opener_keys = {}
    '''
    if len(sys.argv) < 3:
        error("Error: You must specify a source and destination file.")
        exit(1)
    srcPath = sys.argv[1]
    dstPath = sys.argv[2]
    '''
    srcPath = os.path.realpath(os.path.join(repoDir, "Getriebe.scad"))
    dstPath = os.path.realpath(os.path.join(repoDir, "gearlib.scad"))
    if not os.path.isfile(srcPath):
        error("Error: \"{}\" doesn't exist.".format(srcPath))
        exit(1)
    generate_skel(data, doc_opener_keys, 'de')
    load_lang_de(data, doc_opener_keys)
    generate_skel(data, doc_opener_keys, 'en')
    load_lang_en(data, doc_opener_keys)
    error("* writing \"{}\"...".format(dstPath))
    rewrite_as_lang(srcPath, dstPath, data, doc_opener_keys,
                    'de', 'en')

if __name__ == "__main__":
    main()
