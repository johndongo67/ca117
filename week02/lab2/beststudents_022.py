#!/usr/bin/env python3

import sys

names = []

def main():
    try:
        with open(sys.argv[1], "r") as src:

            biggest = -1
            for line in src:
                try:
                    mark = line.strip().split(" ", 1)
                    if int(mark[0]) > biggest and len(names) > 0:
                        names.pop()
                        biggest = int(mark[0])
                        names.append(mark[1])
                    elif int(mark[0]) >= biggest:
                        biggest = int(mark[0])
                        names.append(mark[1])

                except ValueError:
                    print("Invalid mark {:s} encountered. Skipping.".format(mark[0]))

            print("Best student(s):" + " " + ", ".join(names))
            return "Best mark:" + " " + str(biggest)

    except FileNotFoundError:
        return "The file {:s} could not be found".format(sys.argv[1])

if __name__ == '__main__':
    print(main())
