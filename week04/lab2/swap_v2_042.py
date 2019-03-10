#!/usr/bin/env python3

import sys

maps = {}
seen = []

def swap_unique_keys_values(d):
    for k in d.values():
        if k in seen:
            seen.remove(k)
        else:
            seen.append(k)
    for k in d.items():
        if k[1] in seen:
            maps[k[1]] = k[0]
    return maps

if __name__ == '__main__':
    swap_unique_keys_values(d)
