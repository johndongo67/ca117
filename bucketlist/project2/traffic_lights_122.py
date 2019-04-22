#!/usr/bin/env python3

import sys

def red_or_green(d, r, g):
    distance, red, green = d, r, g
    while distance > 0:
        red = r
        while 0 != red:
            distance -= 1
            red -= 1
            if distance == 0:
                return red
        green = g
        while 0 != green:
            green -= 1
            distance -= 1
            if distance == 0:
                return 0

def main():
    x = [line.strip() for line in sys.stdin]
    time = int(x[0])
    lights = [item.split() for item in x[1:]]
    added_time = 0
    for light in lights:
        dis, red, green = int(light[0]), int(light[1]), int(light[2])
        added_time += red_or_green(dis + added_time, red, green)
    print(time + added_time)

if __name__ == '__main__':
    main()
