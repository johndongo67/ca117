import sys
import string

def alph(s):
    alph_str = []
    for i in range(0, len(s) - 1):
        j = i
        while j < len(s) - 1 and s[j] <= s[j + 1]:
            j += 1
        alph_str.append(s[i:j + 1])
    return max(alph_str, key=len)


def main():
    for line in sys.stdin:
        line = line.strip()
        print(alph(line))


if __name__ == '__main__':
    main()
