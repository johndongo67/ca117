#!/usr/bin/env python3

import sys

def main():
    try:
        with open(sys.argv[1], "r") as src:

            biggest = 0
            name = ""
            for line in src:
                try:
                    mark = line.strip()
                    if int(mark[0:2]) > biggest:
                        biggest = int(mark[0:2])
                        name = mark[3:]
                except ValueError:
                    print("Invalid mark {:s} encountered. Skipping.".format(mark[0:2]))

            print("Best student:" + " " + name)
            return "Best mark:" + " " + str(biggest)

    except FileNotFoundError:
        return "The file {:s} could not be found".format(sys.argv[1])


if __name__ == '__main__':
    print(main())
