import sys
import string

def security(s):
    lower = 0
    upper = 0
    digit = 0
    other = 0
    for c in s:
        if c in string.ascii_lowercase:
            lower = 1
        elif c in string.ascii_uppercase:
            upper = 1
        elif c in string.digits:
            digit = 1
        else:
            other = 1
    return lower + upper + digit + other

def main():
    for line in sys.stdin:
        line = line.strip()
        print(security(line))

if __name__ == '__main__':
    main()
