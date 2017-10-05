#!/usr/bin/env python3
"""say hello to the arguments"""

import sys

NUM = len(sys.argv) - 1
NAME = sys.argv


if NUM == 0:
	print('Usage: ' + NAME[0] + ' NAME(S)')
	exit(1)


if NUM == 1:
	print('Hello to the 1 of you: ' + NAME[1] + '!')

if NUM == 2:
        print('Hello to the 2 of you: ' + NAME[1] + ' and ' + NAME[2] + '!')

if NUM > 2:
	print('Hello to the ' + str(NUM) + ' of you: '),
	i = 1
	while i < NUM:
		print(NAME[i], end=', '),
		i = i + 1
	else:
		print('and ' + NAME[i]),
	print('!')
