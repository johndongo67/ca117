#!/usr/bin/env python

import sys

def chop(s):
    s = s[1: - 2]
    return s

def main():
    for lines in sys.stdin.readlines():
        chopped = chop(lines)
        if bool(chopped) == True:
            print (chopped)

if __name__ == '__main__':
    main()
