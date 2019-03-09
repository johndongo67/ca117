#!/usr/bin/env python3

import sys

def security(s):
    lower = 0
    upper = 0
    digits = 0
    other = 0
    for char in s:
        if "0" <= char and char <= "9":
            digits = 1
        elif "a" <= char and char <= "z":
            lower = 1
        elif "A" <= char and char <= "Z":
            upper = 1
        else:
            other = 1
    total = lower + upper + digits + other
    return total


def main():
    for line in sys.stdin:
        password = line.strip()
        print(security(password))

if __name__ == '__main__':
    main()
