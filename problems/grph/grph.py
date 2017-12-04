#!/usr/bin/env python3

import argparse
import sys
import os
from collections import defaultdict

# --------------------------------------------------
def get_args():

    parser = argparse.ArgumentParser(description='Adjacency list')
    parser.add_argument('file', metavar='file', help='DNA strings in FASTA format')
    return parser.parse_args()

# --------------------------------------------------
def main():
    args = get_args()
    file = args.file

    if not os.path.isfile(file):
        print('"{}" is not a file'.format(file))
        sys.exit(1)

## only worked for sample1 and single line sequences    
    ID = []
    string = []
    for line in open(file):
        if "Rosalind" in line:
            ID.append(line[1:-1])
        else:
            string.append(line.strip())


## takes into consideration multi-line sequences
    str2 = []
    temp = []
    first = open(file).readlines()[0]
    last = open(file).readlines()[-1]

    for line in open(file):
        if line != first: 
            if not "Rosalind" in line:
                temp.append(line.strip())
            else:
                str2.append(''.join(temp))
                temp[:] = []
            if line == last: 
                str2.append(''.join(temp))
                temp[:] = []    
            
    DNA = dict(zip(str2, ID))
    prefix = defaultdict(list)
    suffix = defaultdict(list)  

    for seq in str2:
        prefix[seq].append(seq[:3])
        suffix[seq].append(seq[-3:])
    
    for p_key, p_val in prefix.items():
        for s_key, s_val in suffix.items():
            if s_val == p_val and s_key != p_key:
                print('{} {}'.format(DNA[s_key], DNA[p_key]))

# --------------------------------------------------
if __name__ == '__main__':
    main()

