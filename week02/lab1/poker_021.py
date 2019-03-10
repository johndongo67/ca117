#!/usr/bin/env python3

import sys

def prob(total, nothing, one_pair, two_pair, three, straight, flush, full_house, four, straight_flush, royal_flush):
    print("The probability of nothing is {:.4f}%".format(nothing / total * 100))
    print("The probability of one pair is {:.4f}%".format(one_pair / total * 100))
    print("The probability of two pairs is {:.4f}%".format(two_pair / total * 100))
    print("The probability of three of a kind is {:.4f}%".format(three / total * 100))
    print("The probability of a straight is {:.4f}%".format(straight / total * 100))
    print("The probability of a flush is {:.4f}%".format(flush / total * 100))
    print("The probability of a full house is {:.4f}%".format(full_house / total * 100))
    print("The probability of four of a kind is {:.4f}%".format(four / total * 100))
    print("The probability of a straight flush is {:.4f}%".format(straight_flush / total * 100))
    print("The probability of a royal flush is {:.4f}%".format(royal_flush / total * 100))

def main():
    total = 0
    nothing = 0
    one_pair = 0
    two_pair = 0
    three = 0
    straight = 0
    flush = 0
    full_house = 0
    four = 0
    straight_flush = 0
    royal_flush = 0
    for a in sys.stdin:
        a = a.strip().split(",")
        if a[-1] == "9":
            royal_flush = royal_flush + 1
        elif a[-1] == "8":
            straight_flush = straight_flush + 1
        elif a[-1] == "7":
            four = four + 1
        elif a[-1] == "6":
            full_house = full_house + 1
        elif a[-1] == "5":
            flush = flush + 1
        elif a[-1] == "4":
            straight = straight + 1
        elif a[-1] == "3":
            three = three + 1
        elif a[-1] == "2":
            two_pair = two_pair + 1
        elif a[-1] == "1":
            one_pair = one_pair + 1
        else:
            nothing = nothing + 1
        total = total + 1
    return prob(total, nothing, one_pair, two_pair, three, straight, flush, full_house, four, straight_flush, royal_flush)

if __name__ == '__main__':
    main()
