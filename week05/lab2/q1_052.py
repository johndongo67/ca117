#!/usr/bin/env python3

import sys

def main():
    word = sys.argv[1].strip()
    places = int(sys.argv[2])
    while places > 0:
        word = word[-1] + word[0:-1]
        places -= 1
    print(word)

if __name__ == '__main__':
    main()
