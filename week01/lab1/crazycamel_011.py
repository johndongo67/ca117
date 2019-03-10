#!/usr/bin/env python3

import sys

def camel(a):
    i = 0
    b = []
    new_s = ""
    while i < len(a):
        b.append(a[i][0:-1] + a[i][-1].capitalize())
        i = i + 1
    return " ".join(b)

def main():
    for line in sys.stdin:
        a = line.strip().split()
        print(camel(a))

if __name__ == '__main__':
    main()
