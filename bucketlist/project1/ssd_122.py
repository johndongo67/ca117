#!/usr/bin/env python3

import sys

bad_inp = []

def ssd(n, b):
    if n == 0:
        return [0]

    numbers = []
    while n != 0:
        numbers.append(n % b)
        n = n // b

    total = 0
    for k in numbers:
        total = total + k ** 2

    return total

def main():
    total_lines = 1
    try:
        for line in sys.stdin:
            try:
                line = line.strip().split()
                number, base = int(line[0]), int(line[1])
                print(ssd(number, base))

            except:
                bad_inp.append(total_lines)

            total_lines += 1

    finally:
        if len(bad_inp) > 0:
            bad_lines = str(bad_inp[0])
            i = 1
            while i < len(bad_inp):
                bad_lines = bad_lines + ", " + str(bad_inp[i])
                i = i + 1

            print("Failed to convert line(s): {:s} ".format(bad_lines))

if __name__ == '__main__':
    main()
