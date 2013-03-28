class Queue(object):
    def __init__(self):
        self.q = []

    def insert(self, i):
        self.q.append(i)

    def remove(self):
        if len(self.q) == 0:
            raise ValueError()
        first = self.q[0]
        self.q.remove(first)
        return first
