#!/usr/bin/env python3

import sys

def count(b):
    total = 0
    for k in b:
        total = total + 1
    return total

def main():
    total = 0
    seen = []
    for line in sys.stdin:
        a = line.strip().lower()
        for char in a:
            if not char.isalnum():
                a = a.replace(char, " ")
        words = a.split()
        for k in words:
            if k not in seen:
                seen.append(k)
    print(len(seen))

if __name__ == '__main__':
    main()
