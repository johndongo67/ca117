#!/usr/bin/env python3

import sys

contacts = {}

def dict(a):
    i = 0
    while i < len(a):
        contacts[str(a[i])] = a[i + 1]
        i += 2

def main():
    with open(sys.argv[1], "r") as src:
        for line in src:
            line = line.strip().split()
            dict(line)
    for k in sys.stdin:
        if k.strip() in contacts:
            print("Name: " + k.strip())
            print("Phone: " + contacts[k.strip()])
        else:
            print("Name: " + k.strip())
            print("No such contact")

if __name__ == '__main__':
    main()
