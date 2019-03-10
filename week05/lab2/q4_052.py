#!/usr/bin/env python3

import sys

def calorie(f):
    with open(f, "r") as src:
        calories = {}
        for line in src:
            line = line.strip().split()
            calories[line[0]] = line[1]
        return calories

def cal_count(l, d):
    total = 0
    for k in l:
        if k not in d:
            total += 100
        else:
            total += d[k]
    return total

def main():
    people_cals = {}
    cals = calorie(sys.argv[1])
    print(cals)
    info = []
    for line in sys.stdin:
        food = line.strip().split(",")
        info.append(food)

    for line in info:
        people_cals[line[0]] = cal_count(line[1:], cals)

    print(people_cals)

if __name__ == '__main__':
    main()
