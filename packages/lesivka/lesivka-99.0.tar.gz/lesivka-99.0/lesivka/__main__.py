from __future__ import print_function

import argparse
import sys

from . import decode, encode

prog = 'python -m lesivka'
description = 'A simple command line interface for lesivka module.'

parser = argparse.ArgumentParser(prog=prog, description=description)
parser.add_argument("-d", "--decode", action="store_true")
parser.add_argument("-n", "--no-diacritics", action="store_true")
parser.add_argument("text", nargs="*")
options = parser.parse_args()

action = decode if options.decode else encode

if options.text:
    print(action(" ".join(options.text), no_diacritics=options.no_diacritics))
else:
    try:
        for line in sys.stdin:
            print(action(line, no_diacritics=options.no_diacritics), end="")
    except (BrokenPipeError, KeyboardInterrupt):
        pass
