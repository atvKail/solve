class Exercise:
    @staticmethod
    def cond(x: int) -> bool:
        return x % 2 != 0

    operations = []
    results = []
    end = -1

    def __init__(self, operations, end, cond=0):
        self.cond = self.cond if cond == 0 else cond
        self.operations = operations
        self.end = end

    def f(self, heaps: list, p: int) -> bool:
        if any(h <= self.end for h in heaps):
            return p % 2 == 0
        if p == 0:
            return 0
        itResults = []
        for op in self.operations:
            nHeaps = op(heaps)
            itResults.append(self.f(nHeaps, p - 1))
        self.results = itResults
        return any(itResults) if self.cond(p) else all(itResults)


operations = [lambda x: [x[0] - 2], lambda x: [x[0] - 5], lambda x: [x[0] // 3]]
end = 19

exc = Exercise(operations, end)
for s in range(20, 100):
    if exc.f(heaps=[s], p=1) == 0 and exc.f(heaps=[s], p=2) == 1:
        print(s)
        break

cnt = 0
results = []
exc = Exercise(operations, end)
for s in range(20, 100):
    if (
        exc.f(heaps=[s], p=1) == 0
        and exc.f(heaps=[s], p=2) == 0
        and exc.f(heaps=[s], p=3) == 1
    ):
        results.append(s)
        cnt += 1
    if cnt == 2:
        break
print(*results)

exc = Exercise(operations, end)
for s in range(20, 1000):
    if (
        exc.f(heaps=[s], p=1) == 0
        and exc.f(heaps=[s], p=2) == 0
        # and all(exc.results) == 0
        and exc.f(heaps=[s], p=3) == 0
        and exc.f(heaps=[s], p=4) == 1
    ):
        print(s)
        break
