class DividerExercise:
    target = 0
    must_include = 0

    def __init__(self, target, must_include):
        self.target = target
        self.must_include = must_include

    def f(self, x, seen, memo={}):
        if (x, seen) in memo:
            return memo[(x, seen)]
        if x == self.target:
            return 1 if seen else 0
        if x < self.target:
            return 0

        new_seen = seen or (x == self.must_include)

        total = 0
        total += self.f(x - 1, new_seen, memo)
        if x % 2 == 0:
            total += self.f(x // 2, new_seen, memo)
        if x % 3 == 0:
            total += self.f(x // 3, new_seen, memo)

        memo[(x, seen)] = total
        return total

    def sol(self, start):
        return self.f(start, False, {})


ex = DividerExercise(target=11, must_include=57)

print("Задание 23:")
print(ex.sol(122))
