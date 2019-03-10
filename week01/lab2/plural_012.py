#!/usr/bin/env python3

import sys

def plural(s):
    new_s = ""
    if s[-2:] == "ch" or s[-2:] == "sh":
        new_s = s + "es"
    elif s[-1:] == "s" or s[-1:] == "z" or s[-1:] == "x" or s[-1:] == "o":
        new_s = s + "es"
    elif s[-1:] == "y" and s[-2] != "a" and s[-2] != "e" and s[-2] != "i" and s[-2] != "o" and s[-2] != "u":
        new_s = s[0:-1] + "ies"
    elif s[-2:] == "fe":
        new_s = s[0:-2] + "ves"
    elif s[-1:] == "f":
        new_s = s[0:-1] + "ves"
    else:
        new_s = s + "s"
    return new_s


def main():
    for line in sys.stdin:
        single = line.strip()
        print(plural(single))

if __name__ == '__main__':
    main()
