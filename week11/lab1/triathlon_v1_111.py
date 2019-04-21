#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return "Name: {}\nID: {}".format(self.name, self.tid)

class Triathlon(object):

    def __init__(self):
        self.athletes = {}

    def add(self, other):
        self.athletes[other.tid] = other

    def remove(self, other):
        self.athletes.pop(other)

    def lookup(self, other):
        if other in self.athletes:
            return self.athletes[other]
