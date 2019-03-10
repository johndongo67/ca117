#!/usr/bin/env python3

import sys

maps = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
}

tens = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}

teens = {
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
}

def n_to_s(a):
    out = []
    for digit in a:
        if len(digit) == 3:
            out.append("one hundred")
        elif len(digit) == 2 and digit[0] == "1":
            out.append(teens[digit])
        elif len(digit) == 2 and digit[-1] != "0":
            out.append(tens[digit[0]] + "-" + maps[digit[1]])
        elif len(digit) == 2 and digit[-1] == "0":
            out.append(tens[digit[0]])
        else:
            out.append(maps[digit])
    return " ".join(out)

def main():
    for line in sys.stdin:
        line = line.strip().split()
        print(n_to_s(line))

if __name__ == '__main__':
    main()
