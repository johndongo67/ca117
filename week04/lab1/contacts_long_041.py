#!/usr/bin/env python3

import sys

contacts = {}

def dict(a):
    i = 0
    while i < len(a):
        info = (a[1], a[2])
        contacts[str(a[i])] = info
        i += 3

def main():
    with open(sys.argv[1], "r") as src:
        for line in src:
            line = line.strip().split()
            dict(line)
    for k in sys.stdin:
        if k.strip() in contacts:
            print("Name: " + k.strip())
            print("Phone: " + contacts[k.strip()][0])
            print("Email: " + contacts[k.strip()][1])
        else:
            print("Name: " + k.strip())
            print("No such contact")

if __name__ == '__main__':
    main()
