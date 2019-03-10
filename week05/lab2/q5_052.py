#!/usr/bin/env python3

import sys

skipped = []
ranks = {}

def marks(a):
    nums = a[1].split(",")
    total = 0
    try:
        for n in nums:
            total += int(n)
        ranks[a[0]] = total
    except ValueError:
        skipped.append(a[0])

def biggest(t):
    return t[1]

def main():
    for line in sys.stdin:
        line = line.strip().split(":")
        marks(line)

    for k, v in sorted(ranks.items(), key=biggest, reverse=True):
        print(k + " : " + str(v))

    if len(skipped) > 0:
        print("Skipped:")
        for k in skipped:
            print(k)
if __name__ == '__main__':
    main()
