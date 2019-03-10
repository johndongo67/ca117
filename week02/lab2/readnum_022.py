#!/usr/bin/env python3

import sys

names = []

def main():
    for line in sys.stdin:
        try:
            char = line.strip()
            int(char)
            return "Thank you for {:s}".format(char)
        except ValueError:
            print("{:s} is not a number".format(char))

if __name__ == '__main__':
    print(main())
