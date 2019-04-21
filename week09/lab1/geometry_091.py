from math import sqrt

class Shape(object):

    def __init__(self, points):
        self.points = points

    def sides(self):
        side = []
        i = 0
        while i < len(self.points) - 1:
            side.append(self.points[i].distance(self.points[i + 1]))
            i += 1
        side.append(self.points[0].distance(self.points[-1]))
        return side

    def perimeter(self):
        return sum(self.sides())


class Point(Shape):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dist = sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return dist

class Triangle(Shape):

    def area(self):
        l = self.sides()
        s = sum(self.sides()) / 2
        a, b, c = l[0], l[1], l[2]
        area = sqrt((s * (s - a) * (s - b)) * (s - c))
        return area

class Square(Shape):

    def area(self):
        return self.sides()[0] ** 2
