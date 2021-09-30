class stack:
    def __init__(self):
        self.s = []

    def push(self, x):
        if self.s:
            self.s += [(x, min(x, self.s[-1][1]))]
        else:
            self.s += [(x, x)]

    def pop(self):
        if not self.s:
            return -1
        return self.s.pop()[0]

    def getMin(self):
        if not self.s:
            return -1
        return self.s[-1][1]
