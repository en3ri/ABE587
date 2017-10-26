#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
        print('Usage: {} SEQ'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

AA_dict = {}
for line in open("codons.dna"):
	[codon, AA] = line.split(maxsplit=1)
	AA_dict[codon] = AA.split()

AA2_dict = {}
for line in open("codons.rna"):
        [codon, AA] = line.split(maxsplit=1)
        AA2_dict[codon] = AA.split()

SEQ = args[0].upper()
protein = []
k = 3

for i in range(0, len(SEQ), k):
	x = SEQ[i:i+k]
	if x in AA_dict: 
		protein.append(str(AA_dict[x])[2])
	elif x in AA2_dict:
		protein.append(str(AA2_dict[x])[2])

print(''.join(protein))


#To improve: (1) Combine dicts? (2) Improve append
