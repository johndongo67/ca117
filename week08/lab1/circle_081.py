from math import sqrt

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, p):
        return (self.x + p.x) / 2, (self.y + p.y) / 2

    def __str__(self):
        return "({:.1f}, {:.1f})".format(self.x, self.y)

class Circle(object):

    def __init__(self, centre=Point(), radius=0):
        self.centre = centre
        self.radius = radius

    def __str__(self):
        return "Centre: {}".format(self.centre) + "\n" + "Radius: {}".format(self.radius)

    def __add__(self, other):
        return Circle(Point((self.centre.x + other.centre.x) / 2, (self.centre.y + other.centre.y) / 2), self.radius + other.radius)
