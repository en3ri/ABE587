#!/usr/bin/env python3

import sys

args = sys.argv


#Usage Statement
if len(args) < 2:
        print('Usage: {} sequence'.format(args[0]))
        sys.exit(1)

#Main

sequence = str(args[1:])

GC = ('G', 'C', 'g', 'c')
AT = ('A', 'a', 'T', 't')

GC_count = 0
AT_count = 0


for letter in sequence:
	if letter == letter in GC: GC_count = GC_count + 1
	elif letter == letter in AT: AT_count = AT_count + 1


length = GC_count + AT_count
GC_percent = (GC_count / length) * 100


print('{}% GC'.format(int(GC_percent)))
