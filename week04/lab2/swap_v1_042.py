#!/usr/bin/env python3

import sys

maps = {}

def swap_keys_values(d):
    for k in d.items():
        maps[k[1]] = k[0]
    return maps

if __name__ == '__main__':
    swap_keys_values()
