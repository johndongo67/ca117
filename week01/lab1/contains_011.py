#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        line = line.strip().casefold()
        i = 0
        while line[i] != " ":
            i = i + 1
        j = i + i
        k = i
        while j < len(line):
            if line[k:j] == line[:i]:
                print("True")
                break
            j = j + 1
            k = k + 1
        if j == len(line):
            print("False")

if __name__ == '__main__':
    main()
