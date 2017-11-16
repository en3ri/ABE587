#!/usr/bin/env python3

import argparse
import csv
import sys
import os
#from collections import defaultdict

# --------------------------------------------------
def get_args():

    parser = argparse.ArgumentParser(description='Parse BLAST tab')
    parser.add_argument('-p', '--pct_id', help='Percent identity',
                        metavar='float', type=float, default=0)
    parser.add_argument('-e', '--evalue', help='E value float',
                        metavar='float', type=float, default=None)
    parser.add_argument('file', metavar='file', help='BLAST tab output')
    return parser.parse_args()

# --------------------------------------------------
def main():
    args = get_args()
    p = args.pct_id
    e = args.evalue
    file = args.file

    if not os.path.isfile(file):
        print('"{}" is not a file'.format(file))
        sys.exit(1)

    field = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 
                        'qend' 'sstart', 'send', 'bitscore', 'evalue']

    for line in open(file):
        d = dict(zip(field, line.split('\t')))
        row = [d['qseqid'], d['sseqid'], d['pident'], d['evalue']]

        if e is not None and e >= float(d['evalue']) and float(d['pident']) >= p:
            print('\t'.join(row))
        elif e is None and float(d['pident']) >= p:
            print('\t'.join(row))

                  
# --------------------------------------------------
if __name__ == '__main__':
    main()
