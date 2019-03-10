#!/usr/bin/env python3

import sys

def q_no_u(w):
    w = w.lower().replace("qu", "--")
    return "q" in w

def main():
    words = []
    for i in sys.stdin:
        words.append(i.strip())
    qnou = [w for w in words if q_no_u(w) is True]
    print("Words with q but no u: " + str(qnou))

if __name__ == '__main__':
    main()
