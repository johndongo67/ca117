#!/usr/bin/env python3

import sys

times = {}

def seconds(t):
    a = t.split(":")
    sec = int(a[0]) * 60 + int(a[1])
    return sec

def time(n):
    return seconds(n[1])

def main():
    for line in sys.stdin:
        try:
            line = line.strip().split()
            times[line[0]] = min(line[1:], key=seconds)
        except ValueError:
            continue
    k, v = sorted(times.items(), key=time)[0]
    print(k + " : " + v)

if __name__ == '__main__':
    main()
