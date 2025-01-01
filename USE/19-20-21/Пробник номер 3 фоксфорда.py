class Exercise:
    def __init__(self, operations, condition, end):
        self.operations = operations
        self.condition = condition
        self.end = end

    def f(self, heaps, operations, p, end, cond):
        if any(h >= end for h in heaps):
            return p % 2 == 0
        if p == 0:
            return False
        results = []
        for op in operations:
            new_heaps = op(heaps)
            results.append(self.f(new_heaps, operations, p - 1, end, cond))
        return any(results) if cond(p) else all(results)

    def sol(self, heaps, p):
        return self.f(heaps, self.operations, p, self.end, self.condition)


operations = [lambda heaps: [heaps[0] + 1], lambda heaps: [heaps[0] * 2]]
condition = lambda x: x % 2 != 0
end = 169

game = Exercise(operations, condition, end)

for S in range(1, 169):
    if game.sol([S], 1) == 0 and game.sol([S], 2) == 1:
        print("19 задание: S = ", S)
        break

results = []
for S in range(1, 169):
    if game.sol([S], 1) == 0 and game.sol([S], 3) == 1:
        results.append(S)
        if len(results) == 2:
            break

print("20 задание: ответ: ", *results)

for S in range(1, 169):
    if game.sol([S], 2) == 0 and game.sol([S], 4) == 1:
        print("21 задание: S = ", S)
        break
