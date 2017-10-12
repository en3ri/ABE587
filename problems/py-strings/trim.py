#!/usr/bin/env python3

import sys
import os

args = sys.argv

if len(args) < 2:
        print('Usage: {} sequence or *.txt'.format(args[0]))
        sys.exit(1)


if len(args) < 3: X = 5
else: X = int(args[2])

if os.path.isfile(args[1]):
	for line in open(args[1]):
		print(line[0:X])

if not os.path.isfile(args[1]):
	sequence = args[1]
	print(sequence[0:X])

