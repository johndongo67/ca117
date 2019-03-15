#!/usr/bin/env python

import sys

def sumfac(n):
    factors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factors.append(i)
    return sum(factors)

def isPerfect(n):
    return n == sumfac(n)

def main():
    for line in sys.stdin:
        line = int(line.strip())
        print(isPerfect(line))

if __name__ == '__main__':
    main()
