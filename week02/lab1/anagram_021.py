#!/usr/bin/env python3

import sys

def anagram(a):
    if sorted(a[0]) == sorted(a[1]):
        return True
    else:
        return False

def main():
    for line in sys.stdin:
        a = line.strip().split()
        print(anagram(a))


if __name__ == '__main__':
    main()
