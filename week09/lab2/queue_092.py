class Queue(object):

    def __init__(self):
        self.l = []

    def enqueue(self, arg):
        self.l.append(arg)

    def dequeue(self):
        return self.l.pop(0)

    def first(self):
        return self.l[0]

    def __len__(self):
        return len(self.l)

    def is_empty(self):
        return len(self) == 0
