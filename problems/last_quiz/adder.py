#!/usr/bin/env python3

import sys
import os

args = sys.argv[1:]

if len(args) != 2:
        print('Usage: {} arg1 arg2'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

arg1 = args[0]
arg2 = args[1]

if args[0].isdigit(): 
    if args[1].isdigit():
        print(args[0]+args[1])  ## no. need to add . sorry ran out of time. will copy and paste this one and concatenate two strings with an 'and' using {} {} ... and need to actually add. sorru. 



