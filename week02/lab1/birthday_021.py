#!/usr/bin/env python3

import sys
import calendar

def output(day):
    if day == 0:
        return "You were born on a Monday and Monday's child is fair of face."
    elif day == 1:
        return "You were born on a Tuesday and Tuesday's child is full of grace."
    elif day == 2:
        return "You were born on a Wednesday and Wednesday's child is full of woe."
    elif day == 3:
        return "You were born on a Thursday and Thursday's child has far to go."
    elif day == 4:
        return "You were born on a Friday and Friday's child is loving and giving."
    elif day == 5:
        return "You were born on a Saturday and Saturday's child works hard for a living."
    elif day == 6:
        return "You were born on a Sunday and Sunday's child is fair and wise and good in every way."

def main():
    date = int(sys.argv[1])
    month = int(sys.argv[2])
    year = int(sys.argv[3])
    day = calendar.weekday(year, month, date)
    print(output(day))

if __name__ == '__main__':
    main()
