#!/usr/bin/env python3

import sys

def main():
    with open(sys.argv[1], "r") as f:
        censored = f.read().strip().split()

    inp = sys.stdin.read().strip()

    for k in censored:
        inp = inp.replace(k, "@" * len(k))
    print(inp)

if __name__ == '__main__':
    main()
