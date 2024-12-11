class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.build(1, 0, len(arr) - 1)

    def build(self, v, tl, tr):
        if tl == tr:
            self.tree[v] = self.arr[tl]
        else:
            tm = (tl + tr) // 2
            self.build(2 * v, tl, tm)
            self.build(2 * v + 1, tm + 1, tr)
            self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]

    def query(self, v, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        return self.query(2 * v, tl, tm, l, min(r, tm)) + self.query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)

    def update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.tree[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(2 * v, tl, tm, pos, new_val)
            else:
                self.update(2 * v + 1, tm + 1, tr, pos, new_val)
            self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]

class dsu:
    def build_dsu(n):
        global p, sz
        p = [num for num in range(n + 1)]
        sz = [1 for _ in range(n + 1)]

    def pnt(v):
        if p[v] == v:
            return v
        return dsu.pnt(p[v])

    def unit(a, b):
        a = dsu.pnt(a)
        b = dsu.pnt(b)
        if a ==  b:
            return
        if sz[a] > sz[b]:
            a, b = b, a
        p[a] =  b
        sz[b] += sz[a]
