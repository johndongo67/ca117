#!/usr/bin/env python3

import sys

def centre(s):
    return("{:^s}".format(s,len(s)))

def main():
    for line in sys.stdin:
        line = line.strip()
        print(centre(line))

if __name__ == '__main__':
    main()
