class Exercise:
    end = 0
    operations = []
    condition = lambda x: x % 2 == 0

    def __init__(self, operations=None, condition=None, end=0, heaps=1):
        self.operations = operations if operations else []
        self.condition = condition
        self.end = end
        self.heaps = heaps

    def f(self, heaps, operations, p, end, cond):
        if any(h <= end for h in heaps):
            return p % 2 == 0  # True (1), если p чётное

        if p == 0:
            return 0

        results = []
        for op in operations:
            new_heaps = op(heaps)
            if any(x < 0 for x in new_heaps):
                continue
            results.append(self.f(new_heaps, operations, p - 1, end, cond))

        if not results:
            return 0

        return any(results) if cond(p) else all(results)

    def sol(self, heaps, p):
        return self.f(heaps, self.operations, p, self.end, self.condition)


operations = [lambda h: [h[0] - 11], lambda h: [h[0] // 3]]


condition = lambda x: x % 2 != 0

end = 90

ex = Exercise(operations=operations, condition=condition, end=end)

print("Задание 19:")
for S in range(5000, 90, -1):
    if ex.sol([S], 1) == 0 and ex.sol([S], 2) == 1:
        print(S)
        break


print("Задание 20:")
vals_20 = []
for S in range(91, 5001):
    if ex.sol([S], 1) == 0 and ex.sol([S], 3) == 1:
        vals_20.append(S)

if vals_20:
    print(max(vals_20), min(vals_20))


print("Задание 21:")
for S in range(91, 5001):
    if ex.sol([S], 4) == 1 and ex.sol([S], 1) == 0:
        if not ex.sol([S], 2):
            print(S)
            break
