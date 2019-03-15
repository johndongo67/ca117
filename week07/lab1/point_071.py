from math import sqrt

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect(self):
        self.x = -self.x
        self.y = -self.y

    def distance(self, p):
        dist = sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)
        return dist
