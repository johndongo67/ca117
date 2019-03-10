#!/usr/bin/env python3

import sys

dictionary = {}

def l2d(f):
    info = []
    for line in f.readlines():
        line = line.strip().split()
        info.append(line)
    i = 0
    for k in info[0]:
        dictionary[k] = info[1][i]
        i += 1
    return dictionary
