#!/usr/bin/env python3
"""count the vowels in a word"""

import sys

LEN_ARGV = len(sys.argv)
ARGV = sys.argv

print(str(ARGV[1:]))


STRING = ARGV[1:]
LETTER = STRING[0:]
VOWEL = ['a', 'e', 'i', 'o', 'u']

VC = 0


if LEN_ARGV < 2:
        print('Usage: ' + ARGV[0] + ' STRING')
        sys.exit(1)


for LETTER in ('a', 'e', 'i', 'o', 'u'):
        VC = VC + 1
print(VC)
