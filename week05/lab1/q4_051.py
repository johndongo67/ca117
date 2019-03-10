#!/usr/bin/env python3

import sys

def median(a):
    if len(a) % 2 != 0:
        return int(sorted(a)[len(a) // 2])
    else:
        n = int(sorted(a)[len(a) // 2]) + int(sorted(a)[(len(a) // 2) - 1])
        return n / 2

def main():
    nums = [n.strip() for n in sys.stdin]
    total = 0
    for n in nums:
        total += int(n)
    print("Mean: {:.1f}".format(total / len(nums)))
    print("Median: {:.1f}".format(median(nums)))

if __name__ == '__main__':
    main()
