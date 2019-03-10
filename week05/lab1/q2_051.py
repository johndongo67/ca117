#!/usr/bin/env python3

import sys

def contains(s):
    key = ["e", "v", "i", "l"]
    word = [c for c in s if c.lower() in key]
    return word == key

def main():
    words = [line.strip() for line in sys.stdin]
    evil_words = [w for w in words if contains(w.lower()) is True]
    for w in evil_words:
        print(w)


if __name__ == '__main__':
    main()
