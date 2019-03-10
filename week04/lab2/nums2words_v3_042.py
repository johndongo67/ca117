#!/usr/bin/env python3

import sys

map = {}

def n_to_s(a):
    out = []
    for digit in a:
        if int(digit) in map:
            out.append(map[int(digit)])
        else:
            out.append("unknown")
    return " ".join(out)

def main():
    with open(sys.argv[1], "r") as f:
        i = 0
        for k in f:
            trans = k.strip().split()[1]
            map[i] = trans
            i += 1

    for line in sys.stdin:
        line = line.strip().split()
        print(n_to_s(line))

if __name__ == '__main__':
    main()
