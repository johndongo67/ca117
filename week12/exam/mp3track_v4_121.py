
class MP3Track(object):

    def __init__(self, title, duration, artists=None):
        self.title = title
        self.duration = duration
        self.artists = artists

    def to_seconds(self):
        t = self.duration.split(":")
        return int(t[0]) * 60 + int(t[1])

    def add_artist(self, arg):
        if self.artists is None:
            self.artists = [arg]
        else:
            self.artists.append(arg)

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __str__(self):
        a = []
        a.append("Title: {}".format(self.title))
        a.append("By: {}".format(", ".join(self.artists)))
        a.append("Duration: {}".format(self.duration))
        return "\n".join(a)
