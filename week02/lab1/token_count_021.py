#!/usr/bin/env python3

import sys

def count(a):
    total = 0
    for k in a:
        total = total + 1
    return total

def main():
    total = 0
    for line in sys.stdin:
        a = line.strip().split()
        total = count(a) + total
    print(total)

if __name__ == '__main__':
    main()
