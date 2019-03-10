#!/usr/bin/env python3

import sys

def base_10(n, base):
    base = int(base)
    num = int(n, base)
    return num

def main():
    for line in sys.stdin:
        [n, base] = line.strip().split()
        print(base_10(n, base))

if __name__ == '__main__':
    main()
