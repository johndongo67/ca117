#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if len(line) % 2 != 0:
            mid = line[len(line) // 2]
            print(mid)
        else:
            print("No middle character!")

if __name__ == '__main__':
    main()
