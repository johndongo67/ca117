#!/usr/bin/env python3

import sys

def contains(chars, s):
    for k in chars:
        if k in s:
            s = s.replace(k, "", 1)
        else:
            return False
    return True


def main():
    for line in sys.stdin:
        [chars, s] = line.strip().lower().split()
        print(contains(chars, s))

        
if __name__ == '__main__':
    main()
