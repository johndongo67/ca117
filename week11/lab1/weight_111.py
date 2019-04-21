#!/usr/bin/env python3

class Weight(object):

    OUNCES_PER_POUND = 16

    def __init__(self, pounds=0, ounces=0):
        self.pounds = pounds
        self.ounces = ounces

    def from_ounces(self):
        pounds = self // 16
        ounces = self % 16
        return Weight(pounds, ounces)

    def total_ounces(self):
        return (self.pounds * 16) + self.ounces

    def __eq__(self, other):
        return self.total_ounces() == other.total_ounces()

    def __lt__(self, other):
        return self.total_ounces() < other.total_ounces()

    def __le__(self, other):
        return self.total_ounces() <= other.total_ounces()

    def __gt__(self, other):
        return self.total_ounces() > other.total_ounces()

    def __ge__(self, other):
        return self.total_ounces() >= other.total_ounces()

    def __add__(self, other):
        total = self.total_ounces() + other.total_ounces()
        pounds = total // 16
        ounces = total % 16
        return Weight(pounds, ounces)

    def __iadd__(self, other):
        z = self + other
        self.pounds, self.ounces = z.pounds, z.ounces
        return self

    def __mul__(self, other):
        total = Weight(self.pounds * other, self.ounces * other)
        if total.ounces >= 16:
            pounds = total.total_ounces() // 16
            ounces = total.total_ounces() % 16
        else:
            return total

    def __str__(self):
        return "{} pound(s) and {} ounce(s)".format(self.pounds, self.ounces)
