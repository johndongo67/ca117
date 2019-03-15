import sys
from math import sqrt

def roots(l):
    a = float(l[0])
    b = float(l[1])
    c = float(l[2])

    dis = b ** 2 - 4 * a * c

    if dis >= 0:
        r1 = (((-b) + sqrt(dis)) / (2 * a))
        r2 = (((-b) - sqrt(dis)) / (2 * a))
        return "r1 = {}, r2 = {}".format(r1, r2)
    else:
        return None

def main():
    for line in sys.stdin:
        line = line.strip().split()
        print(roots(line))


if __name__ == '__main__':
    main()
