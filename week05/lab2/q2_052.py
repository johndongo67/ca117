#!/usr/bin/env python3

import sys

def contains(s):
    key = ["a", "e", "i", "o", "u"]
    test = [c.lower() for c in s if c.lower() in key]
    return test == key

def main():
    words = [w.strip() for w in sys.stdin]
    new_words = [w for w in words if contains(w) is True]
    for w in new_words:
        print(w)

if __name__ == '__main__':
    main()
