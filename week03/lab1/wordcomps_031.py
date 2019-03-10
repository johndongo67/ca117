#!/usr/bin/env python3

import sys

def vowels(w):
    return "a" in w and "i" in w and "e" in w and "o" in w and "u" in w

def counts(a):
    total = 0
    for k in a:
        if k.lower().count("e") > total:
            total = k.lower().count("e")
    return total

def main():
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    total_e = counts(words)
    w17 = [w for w in words if len(w) == 17]
    w18 = [w for w in words if len(w) > 17]
    vowel = [w for w in words if vowels(w.lower()) is True]
    svowel = sorted(vowel, key=len)
    w4a = [w for w in words if w.lower().count("a") == 4]
    w2q = [w for w in words if w.lower().count("q") >= 2]
    wcie = [w for w in words if "cie" in w.lower()]
    wan = [w for w in words if sorted("angle") == sorted(w.lower()) and w != "angle"]
    wiary = [w for w in words if w.lower()[-4:] == "iary"]
    wme = [w for w in words if w.lower().count("e") == total_e]

    print("Words containing 17 letters: " + str(w17))
    print("Words containing 18+ letters: " + str(w18))
    print("Shortest word containing all vowels: " + str(svowel[0]))
    print("Words with 4 a's: " + str(w4a))
    print("Words with 2+ q's: " + str(w2q))
    print("Words containing cie: " + str(wcie))
    print("Anagrams of angle: " + str(wan))
    print("Words ending in iary: " + str(len(wiary)))
    print("Words with most e's: " + str(wme))

if __name__ == '__main__':
    main()
