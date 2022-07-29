#!/usr/bin/env python3
import sys
import os
import re
# import string
import hashlib
import pathlib

MODULE_DIR = os.path.dirname(__file__)
REPO_DIR = os.path.dirname(__file__)  # same as MODULE_DIR in this case
REPOS_DIR = os.path.dirname(REPO_DIR)

import pyopenscad
# from pyopenscad.scad import (
#     ScadAnalyser,
# )
from pyopenscad import (
    echo0,
    echo1,
    echo2,
    done_args,
)


try:
    import pycodetool
except ImportError as ex:
    # ^ Python 3 ModuleNotFoundError is a subclass of ImportError
    if (("No module named 'pycodetool'" in str(ex))  # Python 3
            or ("No module named pycodetool" in str(ex))):  # Python 2
        try_repo_dir = os.path.join(REPOS_DIR, "pycodetool")
        ok_flag = os.path.join(try_repo_dir, "pycodetool", "__init__.py")
        if os.path.isfile(ok_flag):
            sys.path.insert(0, try_repo_dir)
        else:
            pass
            # echo0("Error: There is no pycodetool.")
    else:
        raise ex

# from pycodetool.csharp import (
#    test_file,
# )

try:
    import sca2d
except ImportError as ex:
    if (("No module named 'pycodetool'" in str(ex))  # Python 3
            or ("No module named pycodetool" in str(ex))):  # Python 2
        HOME = pathlib.Path.home()
        DOWNLOADS = os.path.join(HOME, "Downloads")
        TRY_BATH = os.path.join(DOWNLOADS, "git",
                                "bath_open_instrumentation_group")
        TRY_SCA2D = os.path.join(TRY_BATH, "sca2d")
        if os.path.isfile(os.path.join(TRY_SCA2D, "sca2d",
                                       "__init__.py")):
            echo0('* using sca2d from the "" repo.'.format(TRY_SCA2D))
            sys.path.insert(0, TRY_SCA2D)
        else:
            echo0("Error: no sca2d")
            raise ex
    else:
        raise ex

from sca2d import Analyser
from sca2d.messages import (
    print_messages,
    count_messages,
    gitlab_summary,
)

wordPattern = re.compile(r'[\W_]+')
encoding = 'utf-8'

HOME = pathlib.Path.home()
SCAD_GRAM_PATH = os.path.join(HOME, "Downloads", "git",
                              "bath_open_instrumentation_group",
                              "sca2d", "sca2d", "lark", "scad.lark")

UPSTREAM_PATH = os.path.join(REPO_DIR, "Getriebe.scad")


# shares some code with io_csharptopython.io_csharp_to_python_file
def _generate_meta(path, analyser, dest_dir, out_name=None):
    '''
    Sequential arguments:
    output_tree -- dest_dir where to save the output
    '''

    # Cited examples are from
    # <https://gitlab.com/bath_open_instrumentation_group/sca2d>.

    # See _run_on_file in sca2d/sca2d/__main__.py for an example.
    if out_name is None:
        name = os.path.split(path)[1]
        nameNoExt, dotExt = os.path.splitext(name)
        out_name = nameNoExt + ".tree.txt"
    dst_file = os.path.join(dest_dir, out_name)
    [parsed, all_messages] = analyser.analyse_file(
        path,
        output_tree=dst_file,
    )

    # See main in sca2d/sca2d/__main__.py for an example:
    print_messages(all_messages, args.file_or_dir_name, args.colour, args.debug)
    message_summary = count_messages(all_messages)
    print(message_summary)
    with open("gl-code-quality-report.json", "w") as json_file:
        json.dump(gitlab_summary(all_messages), json_file)

    # TODO: useful things here
    # print("cat <<END")
    # tab = "    "
    # print("END")

    # See example at sca2d/sca2d/__main__.py>
    # return [parsed, all_messages]
    if (message_summary.fatal + message_summary.error) > 0:
        return 1
    return 0


def generate_meta(in_path):
    dest_dir = os.path.dirname(in_path)

    # See example at
    # <https://
    # gitlab.com/bath_open_instrumentation_group/sca2d/-/blob/master/
    # sca2d/__main__.py>
    verbose = True if verbosity > 0 else False
    # TODO: analyser = ScadAnalyser(SCAD_GRAM_PATH, verbose=verbose)
    analyser = Analyser(verbose=args.verbose)
    _generate_meta(
        UPSTREAM_PATH,
        analyser,
        dest_dir,
        # out_name="geardrive.scad",
    )


def main():
    in_path = None
    for argI in range(1, len(sys.argv)):
        arg = sys.argv[argI]
        if arg.startswith("-"):
            if arg in done_args:
                pass
            else:
                echo0("Error: The argument {} is invalid.".format(arg))
                return 1
        elif in_path is None:
            if not os.path.isfile(arg):
                echo0(
                    'Error: You must either specify a file or not'
                    ' specify an argument'
                    ' (to leave the default file "{}")'
                    ''.format(UPSTREAM_PATH)
                )
                return 1
            in_path = arg

    if in_path is None:
        # echo0("You must specify a file in SCAD format"
        #       " (or another format with C-like comments).")
        # return 1
        in_path = UPSTREAM_PATH
    # from pyopenscad.scrape import dump_comments
    # return dump_comments(sys.argv[1])
    return test(in_path=in_path)


if __name__ == "__main__":
    sys.exit(main())
