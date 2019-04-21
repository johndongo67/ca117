class Time(object):

    def __init__(self, hour=00, minute=00, second=00):
        self.hour = hour
        self.minute = minute
        self.second = second

    def to_seconds(self):
        return (self.hour * 60 * 60) + (self.minute * 60) + self.second

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __str__(self):
        return "The time is {:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __add__(self, other):
        hour = self.hour + other.hour
        if hour > 24:
            hour -= 24
        minute = self.minute + other.minute
        if minute > 60:
            minute -= 60
            hour += 1
        second = self.second + other.second
        if second > 60:
            second -= 60
            minute += 1
        return Time(hour, minute, second)

    def __iadd__(self, other):
        z = self + other
        self.hour, self.minute, self.second = z.hour, z.minute, z.second
        return self

    @classmethod
    def seconds_to_time(cls, s):
        minute, second = divmod(s, 60)
        hour, minute = divmod(minute, 60)
        overflow, hour = divmod(hour, 24)
        return Time(hour, minute, second)
