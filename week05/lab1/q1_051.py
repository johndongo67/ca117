#!/usr/bin/env python3

import sys

def main():
    a = list(sys.argv[1].strip())
    for i in range(1, len(a), 2):
        a[i - 1], a[i] = a[i], a[i - 1]
    print("".join(a))

if __name__ == '__main__':
    main()
