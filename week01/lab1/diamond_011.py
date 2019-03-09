#!/usr/bin/env python3

import sys

def main():
    n = int(sys.argv[1])

    for k in range(1, 2 * n):
        spaces = abs(k - n)
        line = ' ' * spaces + '* ' * (n - spaces)
        print(line[0:-1])

if __name__ == '__main__':
    main()
