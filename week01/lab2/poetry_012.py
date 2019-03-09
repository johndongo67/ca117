#!/usr/bin/env python3

import sys

a = []

def centre(a, n):
    i = 0
    while i < len(a):
        print("{:^{}s}".format(a[i], n))
        i = i + 1

def main():
    for line in sys.stdin:
        line = line.strip()
        a.append(line)

    longest = 0
    i = 0
    while i < len(a):
        if len(a[i]) > longest:
            longest = len(a[i])
        i = i + 1

    return centre(a, longest)


if __name__ == '__main__':
    main()
