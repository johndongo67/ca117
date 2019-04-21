import sys
from math import sqrt
from stack_092 import Stack

def calculator(line):
    items = line.split()
    nums = Stack()
    for k in items:
        if k.isdecimal() or "." in k:
            nums.push(float(k))
        elif k == "*":
            fin = nums.l[-2] * nums.l[-1]
            nums.pop()
            nums.pop()
            nums.push(fin)
        elif k == "+":
            fin = nums.l[-2] + nums.l[-1]
            nums.pop()
            nums.pop()
            nums.push(fin)
        elif k == "-":
            fin = nums.l[-2] - nums.l[-1]
            nums.pop()
            nums.pop()
            nums.push(fin)
        elif k == "/":
            fin = nums.l[-2] / nums.l[-1]
            nums.pop()
            nums.pop()
            nums.push(fin)
        elif k == "r":
            fin = sqrt(nums.l[-1])
            nums.pop()
            nums.push(fin)
        elif k == "n":
            fin = -nums.l[-1]
            nums.pop()
            nums.push(fin)

    return nums.l[0]
