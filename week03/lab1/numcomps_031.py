#!/usr/bin/env python3

import sys

def is_prime_number(n):
    if n == 1:
        return False
    elif n == 4:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False

    return True

def main():
    numbers = []
    for i in range(1, int(sys.argv[1]) + 1):
        numbers.append(i)
    print("Multiples of 3: " + str([n for n in numbers if n % 3 == 0]))
    print("Multiples of 3 squared: " + str([n ** 2 for n in numbers if n % 3 == 0]))
    print("Multiples of 4 doubled: " + str([n * 2 for n in numbers if n % 4 == 0]))
    print("Multiples of 3 or 4: " + str([n for n in numbers if n % 3 == 0 or n % 4 == 0]))
    print("Multiples of 3 and 4: " + str([n for n in numbers if n % 3 == 0 and n % 4 == 0]))
    print("Multiples of 3 replaced: " + str(["X" if n % 3 == 0 else n for n in numbers]))
    print("Primes: " + str([n for n in numbers if is_prime_number(n) is True]))

if __name__ == '__main__':
    main()
