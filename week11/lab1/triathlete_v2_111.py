#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.times = {}

    def add_time(self, sport, time):
        self.times[sport] = time

    def get_time(self, sport):
        return self.times[sport]

    def __str__(self):
        return "Name: {}\nID: {}\nRace time: {}".format(self.name, self.tid, sum(self.times.values()))
