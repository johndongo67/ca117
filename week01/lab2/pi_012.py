#!/usr/bin/env python3

import sys
import math

def places(n):
    print("{:.{}f}".format(math.pi,n))

def main():
    n = int(sys.argv[1])
    return places(n)


if __name__ == '__main__':
    main()
