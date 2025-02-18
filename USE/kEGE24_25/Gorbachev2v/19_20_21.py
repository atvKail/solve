import sys

sys.setrecursionlimit(10000)


class Exercise:
    def __init__(self, operations=None, condition=None, end=15, heaps=2):
        self.operations = operations if operations is not None else []
        self.condition = condition
        self.end = end
        self.heaps = heaps
        self.memo = {}

    def f(self, heaps, p):
        key = (tuple(heaps), p)
        if key in self.memo:
            return self.memo[key]

        if any(h < self.end for h in heaps):
            result = p % 2 == 0
            self.memo[key] = result
            return result

        if p == 0:
            self.memo[key] = False
            return False

        results = []
        for op in self.operations:
            new_heaps = op(heaps)

            if any(x < 0 for x in new_heaps):
                continue
            results.append(self.f(new_heaps, p - 1))

        if not results:
            result = False
        else:
            if self.condition(p):
                result = any(results)
            else:
                result = all(results)

        self.memo[key] = result
        return result

    def sol(self, heaps, p):
        self.memo.clear()
        return self.f(heaps, p)


operations = []
for i in range(2):
    operations.append(
        lambda heaps, i=i: [
            heaps[j] - 2 if j == i else heaps[j] for j in range(len(heaps))
        ]
    )

    operations.append(
        lambda heaps, i=i: [
            heaps[j] // 3 if j == i else heaps[j] for j in range(len(heaps))
        ]
    )

condition = lambda p: (p % 2 != 0)
end = 15

ex = Exercise(operations=operations, condition=condition, end=end, heaps=2)


def next_positions(heaps):
    res = []
    for i in range(len(heaps)):
        if heaps[i] >= 2:
            new_heaps = list(heaps)
            new_heaps[i] -= 2
            res.append(tuple(new_heaps))

        if heaps[i] >= 3:
            new_heaps = list(heaps)
            new_heaps[i] //= 3
            res.append(tuple(new_heaps))
    return res


def can_petya_end_in_one_move(heaps, end=15):
    for pos in next_positions(heaps):
        if any(h < end for h in pos):
            return True
    return False


def can_win_in_two_after_vanya_error(S):
    start = (S, S)

    for p1 in next_positions(start):
        if any(h < end for h in p1):
            continue

        for p2 in next_positions(p1):
            if can_petya_end_in_one_move(p2, end):
                return True

    return False


print("Задание 19:")
S_19 = None
for S in range(15, 5000):
    if (not ex.sol((S, S), 1)) and ex.sol((S, S), 2):
        S_19 = S
        print(S_19)
        break
if S_19 is None:
    print("Не найдено S в заданном диапазоне для задания 19")


print("Задание 20:")
vals_20 = []
for S in range(15, 5000):
    cond1 = not ex.sol((S, S), 1)

    cond2 = can_win_in_two_after_vanya_error(S)

    if cond1 and cond2:
        vals_20.append(S)

if vals_20:
    print("Максимальное S =", max(vals_20))
else:
    print("Нет подходящих S для задания 20.")


print("Задание 21:")
S_21 = None
for S in range(15, 5000):
    if ex.sol((S, S), 4) and (not ex.sol((S, S), 1)) and (not ex.sol((S, S), 2)):
        S_21 = S

if S_21 is not None:
    print(S_21)
else:
    print("Не найдено S для задания 21")
