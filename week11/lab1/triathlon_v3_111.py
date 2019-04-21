#!/usr/bin/env python3

#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.times = {}

    def __eq__(self, other):
        return sum(self.times.values()) == sum(other.times.values())

    def __gt__(self, other):
        return sum(self.times.values()) > sum(other.times.values())

    def __lt__(self, other):
        return sum(self.times.values()) < sum(other.times.values())

    def add_time(self, sport, time):
        self.times[sport] = time

    def get_time(self, sport):
        return self.times[sport]

    def __str__(self):
        return "Name: {}\nID: {}\nRace time: {}".format(self.name, self.tid, sum(self.times.values()))

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

    def best(self):
        return sorted(self.athletes.values())[0]

    def worst(self):
        return sorted(self.athletes.values())[-1]

    def __str__(self):
        out = []
        for triathlete in sorted(self.athletes.values(), key=sorter):
            out.append("Name: {}".format(triathlete.name))
            out.append("ID: {}".format(triathlete.tid))
        return "\n".join(out)

def sorter(t):
        return t.name
