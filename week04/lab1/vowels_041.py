#!/usr/bin/env python3

import sys

vow_freq = {
    "e": 0,
    "a": 0,
    "i": 0,
    "o": 0,
    "u": 0,
}

def freq(a):
    for k in vow_freq:
        for w in a:
            vow_freq[k] += w.count(k)

def min_width(l):
    num_width = 0
    for item in l:
        if num_width < len(str(item[1])):
            num_width = len(str(item[1]))
    return num_width

def big_sort(t):
    return t[1]

def main():
    words = []
    for line in sys.stdin:
        line = line.strip().lower().split()
        for k in line:
            words.append(k)
    freq(words)
    num_width = min_width(vow_freq.items())
    for k in sorted(vow_freq.items(), key=big_sort, reverse=True):
        print("{:>s} : {:{:d}d}".format(k[0], k[1], num_width))


if __name__ == '__main__':
    main()
