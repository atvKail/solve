import sys

sys.setrecursionlimit(6000)

operations = [
    lambda heaps: [heaps[0] + 2, heaps[1]],
    lambda heaps: [heaps[0] * 3, heaps[1]],
    lambda heaps: [heaps[0], heaps[1] + 2],
    lambda heaps: [heaps[0], heaps[1] * 3],
]


def win1(heaps, move):
    if sum(heaps) >= 95:
        return 1 if (move - 1) & 1 != 0 else 0

    if move == 3:
        return any(sum(op(heaps)) >= 95 for op in operations)

    if move % 2 == 1:
        return any(win1(op(heaps), move + 1) for op in operations)
    else:
        return all(win1(op(heaps), move + 1) for op in operations)


for s in range(1, 88):
    heaps = [6, s]
    if win1(heaps, 1) == 1:
        print("19 ->", s)
        break


def win2(heaps, move):
    if move > 4:
        return 0
    if move < 3 and sum(heaps) >= 95:
        return 0
    if sum(heaps) >= 95:
        return 1

    if move & 1 > 0:
        return any([win2(op(heaps), move + 1) for op in operations])
    else:
        return all([win2(op(heaps), move + 1) for op in operations])


print("20: ")
cnt = 0
for s in range(1, 88):
    heaps = [6, s]
    if win2(heaps, 0) == 0 and win2(heaps, 1) == 1 and win2(heaps, 2) == 1:
        print(s)
        cnt += 1
    if cnt == 2:
        break


print("21: ")


def can_vanya_win_by_move4(state):
    for op_petya in operations:
        state_after_petya = op_petya(state)
        if not any(sum(op_vanya(state_after_petya)) >= 95 for op_vanya in operations):
            return False
    return True


results = []
for s in range(1, 88):
    heaps = [6, s]

    petya_moves = [op(heaps) for op in operations]

    cond_no_immediate_vanya = any(
        all(sum(op_vanya(state)) < 95 for op_vanya in operations)
        for state in petya_moves
    )

    cond_vanya_strategy = all(
        any(
            (sum(state_after_vanya) >= 95)
            or (
                sum(state_after_vanya) < 95
                and can_vanya_win_by_move4(state_after_vanya)
            )
            for state_after_vanya in [op_vanya(state) for op_vanya in operations]
        )
        for state in petya_moves
    )

    if cond_vanya_strategy and cond_no_immediate_vanya:
        results.append(s)

if results:
    print(" ".join(map(str, [min(results), max(results)])))
else:
    print("Нет решений")
