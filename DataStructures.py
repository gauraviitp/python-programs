from math import inf
import operator

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(x)
        return self.parent[x]
        
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            # attach tree of lower rank to the tree of higher rank
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]

class FenwickTree:
    def __init__(self, n: int, op):
        self.n = n
        self.op = self.get_op()
        self.init_val = self.get_init_val()
        self.bit = [self.init_val] * n

    def get_op(self):
        return operator.add

    def get_init_val(self):
        return 0

    @classmethod
    def from_list(cls, a: list, op):
        n = len(a)
        obj = cls(n, op)
        for i in range(n):
            obj.update(i, a[i])
        return obj

    def update(self, index, delta):
        while index < self.n:
            self.bit[index] = self.op(self.bit[index], delta)
            index = index | (index + 1)

    def get(self, r):
        res = self.init_val
        while r >= 0:
            res = self.op(res, self.bit[r])
            r = (r & (r + 1)) - 1
        return res

    def get_range(self, l, r):
        if self.op == min:
            raise Exception('min is not reversible')
        return self.get(r) - self.get(l - 1)


class FenwickTreeMin(FenwickTree):
    def get_op(self):
        return min
    
    def get_init_val(self):
        return inf

class FenwickTree2D:
    def __init__(self, nx: int, ny: int):
        self.nx = nx
        self.ny = ny
        self.op = self.get_op()
        self.init_val = self.get_init_val()
        self.bit = [[self.init_val for i in range(ny)] for j in range(nx)]

    @classmethod
    def from_list(cls, a):
        nx = len(a)
        ny = 0
        if nx > 0: ny = len(a[0])
        obj = cls(nx, ny)
        for i in range(nx):
            for j in range(ny):
                obj.update(i, j, a[i][j])
        return obj

    def get_op(self):
        return operator.add

    def get_init_val(self):
        return 0

    def update(self, x, y, delta):
        i, j = x, y
        while i < self.nx:
            j = y
            while j < self.ny:
                self.bit[i][j] = self.op(self.bit[i][j], delta)
                j = j | (j + 1)
            i = i | (i + 1)

    def get(self, x, y):
        i, j = x, y
        res = self.init_val
        while i >= 0:
            j = y
            while j >= 0:
                res = self.op(res, self.bit[i][j])
                j = (j & (j + 1)) - 1
            i = (i & (i + 1)) - 1
        return res

    def get_range(self, l, x1, y1, x2, y2):
        if self.op == min:
            raise Exception('min is not reversible')
        return self.get(x2, y2) - self.get(x1 - 1, y1 - 1)

class FenwickTree2DMin(FenwickTree2D):
    def get_op(self):
        return min
    
    def get_init_val(self):
        return inf

