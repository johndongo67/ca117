#!/usr/bin/env python3

import sys

def capitals(w):
    nl = []
    for char in w:
        if char.isupper() is False:
            nl.append(" ")
        else:
            nl.append(char)
    s = "".join(nl)
    return max(s.split(), key=len)


def main():
    words = [line.strip() for line in sys.stdin]
    for w in words:
        print(capitals(w))

if __name__ == '__main__':
    main()
