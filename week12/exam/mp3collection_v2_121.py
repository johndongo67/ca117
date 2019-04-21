
class MP3Track(object):

    def __init__(self, title, duration, artists):
        self.title = title
        self.duration = duration
        self.artists = artists

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
