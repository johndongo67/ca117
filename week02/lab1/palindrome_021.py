#!/usr/bin/env python3

import sys

def palindrome(s):
    new_s = ""
    for k in s:
        if k.isalnum() is True:
            new_s = new_s + k
    rev_s = new_s[::-1]
    if rev_s == new_s:
        return True
    else:
        return False

def main():
    for line in sys.stdin:
        s = line.strip().lower()
        print(palindrome(s))


if __name__ == '__main__':
    main()
