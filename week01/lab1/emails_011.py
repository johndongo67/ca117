#!/usr/bin/env python3

import sys

def names(a):
    i = 0
    while a[1][i] and (a[1][i] < "0" or "9" < a[1][i]):
        i = i + 1
    return a[0].capitalize() + " " + a[1][:i].capitalize()

def main():
    for line in sys.stdin:
        a = line.strip().split(".")
        print(names(a))

if __name__ == '__main__':
    main()
