#!/usr/bin/env python3

import sys

map = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
}

def n_to_s(a):
    out = []
    for digit in a:
        out.append(map[digit])
    return " ".join(out)

def main():
    for line in sys.stdin:
        line = line.strip().split()
        print(n_to_s(line))

if __name__ == '__main__':
    main()
