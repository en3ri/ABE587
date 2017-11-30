#!/usr/bin/env python3

import sys
import os

args = sys.argv[1:]

if len(args) != 2:
    print('Usage: {} arg1 arg2'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

arg1 = args[0]
arg2 = args[1]

if arg1.isdigit() and arg2.isdigit():
    print(int(arg1)+int(arg2))

elif not arg1.isdigit() and not arg2.isdigit():
    print('{} and {}'.format(args[0], args[1]))

else: 
    print('Cannot combine number and string')
    sys.exit(1)


#Sorry, this is a re-commit. I committed in class as well.
#I wasn't done because I tried argparse at first.. and I'm typically slow
