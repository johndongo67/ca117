from math import sqrt

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, p):
        dist = sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)
        return dist

    def __str__(self):
        return "({:.1f}, {:.1f})".format(self.x, self.y)

class Segment(object):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
        return Point((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2)

    def length(self):
        dist = sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)
        return dist

class Circle(object):

    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def overlaps(self, arg):
        seg = Segment(self.centre, arg.centre)
        dist = seg.length()
        if dist < self.radius + arg.radius:
            return True
        else:
            return False
