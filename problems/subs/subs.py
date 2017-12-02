#!/usr/bin/env python3

import argparse
import sys
import os

# --------------------------------------------------
def get_args():

    parser = argparse.ArgumentParser(description='Position(s) of sub-string in string')
    parser.add_argument('s', metavar='string', help='string')
    parser.add_argument('t', metavar='string', help='sub-string')
    return parser.parse_args()

# --------------------------------------------------
def main():
    args = get_args()
    s = args.s
    t = args.t

    if len(t[0:]) > len(s[0:]):
        print('String must be longer than sub-string')
        sys.exit(1)
    
    position = []
    kmer = len(t[0:])
    j = 0
    k = j + kmer

    for symbols in s:
        if s[j:k] == t:
            position.append(j+1)
        j += 1
        k = j + kmer

    if not position:
        print('Not found')
    else:
        print(*position)

# --------------------------------------------------
if __name__ == '__main__':
    main()
