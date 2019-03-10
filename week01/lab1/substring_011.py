#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        [key, s] = line.strip().lower().split()
        if key in s:
            print(True)
        else:
            print(False)

        
if __name__ == '__main__':
    main()
