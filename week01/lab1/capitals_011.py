#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if len(line) >= 2:
            new_s = line[0].capitalize() + line[1:-1] + line[-1].capitalize()
            print(new_s)

if __name__ == '__main__':
    main()
