#!/usr/bin/env python3
"""say hello to the arguments"""

import sys

args = sys.argv
NUM = len(args)
NUM2 = len(args) - 1

if NUM < 2:
	print('Usage: {} NAME [NAME2 ...]'.format(args[0]))
	sys.exit(1)


if NUM == 2:
	print('Hello to the 1 of you: {}!'.format(args[1]))

if NUM == 3:
        print('Hello to the 2 of you: {}!'.format(' and '.join(args[1:])))

if NUM > 3:
        print('Hello to the {} of you: {}, and {}!'
		.format(NUM2, ', '.join(args[1:-1]), args[-1]))
