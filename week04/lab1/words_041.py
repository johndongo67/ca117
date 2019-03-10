#!/usr/bin/env python3

import sys
import string

word_freq = {}

def punc(l):
    new_words = []
    s = ""
    for w in l:
        i = len(w) - 1
        if w[i] in string.punctuation:
            while i > 0 and w[i] in string.punctuation:
                s = w[0:i]
                i -= 1
            new_words.append(s)
        else:
            new_words.append(w)
    return new_words


def freq(a):
    for w in a:
        if w not in word_freq:
            word_freq[w] = 1
        else:
            word_freq[w] = word_freq[w] + 1

def main():
    for line in sys.stdin:
        words = line.strip().lower().split()
        freq(punc(words))
    for k in sorted(word_freq.items()):
        print("{:s} : {:d}".format(k[0], k[1]))


if __name__ == '__main__':
    main()
