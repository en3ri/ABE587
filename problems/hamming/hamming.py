#!/usr/bin/env python3

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    parser=argparse.ArgumentParser(description='Hamming script')
    parser.add_argument('s', help='String 1',
                        metavar='str', type=str, default='')
    parser.add_argument('t', help='String 2 of equal length',
                        metavar='str', type=str, default='')
    return parser.parse_args()

# --------------------------------------------------
def main():
    args = get_args()
    s = "{}     ".format(args.s)
    t = "{}     ".format(args.t)

#   if len(s) != len(t):
#       parser.print_help()
#       sys.exit(1)        

    count = 0
    x = 0
    for letter in s:
        if letter != t[x]:
            count += 1
        x += 1 

    print(count)   

# --------------------------------------------------
if __name__ == '__main__':
    main()
