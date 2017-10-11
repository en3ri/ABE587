#!/usr/bin/env python3
"""count the vowels in a word"""

import sys

args = sys.argv


#Usage Statement
if len(args) < 2:
	print('Usage: {} STRING'.format(args[0]))
	sys.exit(1)

#Main

STRING = ' '.join(args[1:])

VOWELS = ('a', 'e', 'i', 'o', 'u')
VC = 0

for letter in STRING:
	if letter == letter in VOWELS: VC = VC + 1


if VC == 1:
        print('There is {} vowel in "{}."'.format(VC, STRING))
else:
	print('There are {} vowels in "{}."'.format(VC, STRING))
