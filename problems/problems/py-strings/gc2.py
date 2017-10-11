#!/usr/bin/env python3

import sys
import os

args = sys.argv


#Usage Statement
if len(args) < 2:
        print('Usage: {} file.txt'.format(args[0]))
        sys.exit(1)

if not os.path.isfile(args[1]):
        print('"{}" is not a file'.format(args[1]))
        sys.exit(1)

#Main

GC = ('G', 'C', 'g', 'c')
AT = ('A', 'a', 'T', 't')

#sequence = str(args[1:])

for line in open(args[1]):

	GC_count = 0
	AT_count = 0

	for letter in line:
        	if letter == letter in GC: GC_count = GC_count + 1
        	elif letter == letter in AT: AT_count = AT_count + 1
	
	length = GC_count + AT_count
	GC_percent = (GC_count / length) * 100

	print('{}'.format(int(GC_percent)))
