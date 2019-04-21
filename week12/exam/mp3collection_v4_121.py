
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

class MP3Collection(object):

    def __init__(self):
        self.d = {}

    def add(self, other):
        self.d[other.title] = other

    def remove(self, other):
        del self.d[other]

    def get_mp3s_by_artist(self, other):
        tracks = []
        for mp3 in self.d.values():
            if other in mp3.artists:
                tracks.append(mp3)
        return tracks

    def lookup(self, other):
        if other in self.d:
            return self.d[other]

    def __add__(self, other):
        c = MP3Collection()
        for k in other.d:
            if k not in self.d:
                self.d[k] = other.d[k]
        c.d = self.d
        return c

    def __str__(self):
        a = []
        for mp3 in sorted(self.d.values()):
            a.append(str(mp3))

        return "\n".join(a)
