#!/usr/bin/env python3

import sys
import os
from collections import Counter

args = sys.argv[1:]

if len(args) != 2:
	print('Usage: {} LEN STR'.format(os.path.basename(sys.argv[0])))
	sys.exit(1)

LEN = args[0]
STR = args[1].upper()
LEN_STR = int(len(STR))

if len(args) == 2:
	if not args[0].isdigit():
        	print('Kmer size "{}" is not a number'.format(args[0]))
        	sys.exit(1)
	if int(LEN) < 1:
		print('Kmer size "{}" must be > 0'.format(LEN))
		sys.exit(1)
	if int(LEN) > LEN_STR:
		print('There are no {}-mers in "{}"'.format(LEN, STR))
		sys.exit(1)

# number of kmers
N = LEN_STR - int(LEN) + 1
L = int(LEN)

kmer = []
i = 0

for i in range(0, N):
	x = STR[i:L]
	i += 1
	L += 1
	kmer.append(x)

print(STR)

count = Counter(kmer)

for kmer in sorted(count.keys()):
	print('{} {}'.format(kmer, count[kmer]))
