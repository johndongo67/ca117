
class MP3Track(object):

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return "Title: {}\nDuration: {}".format(self.title, self.duration)

class MP3Collection(object):

    def __init__(self):
        self.d = {}

    def add(self, other):
        self.d[other.title] = other

    def remove(self, other):
        del self.d[other]

    def lookup(self, other):
        if other in self.d:
            return self.d[other]
