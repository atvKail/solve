operations = {
    "A": lambda x: x + 1,
    "B": lambda x: x * 2,
    "C": lambda x: x * x,
}


def f(x, nseen40, seen80, prev_op=None, memo={}):
    if (x, nseen40, seen80, prev_op) in memo:
        return memo[(x, nseen40, seen80, prev_op)]
    if x == 155:
        return 1 if nseen40 and seen80 else 0
    if x > 155:
        return 0

    nnseen40 = nseen40 and (x != 40)
    nseen80 = seen80 or (x == 80)

    total = 0
    for op_name, op in operations.items():
        if prev_op == "B" and op_name == "B":
            continue

        total += f(op(x), nnseen40, nseen80, op_name, memo)

    memo[(x, nseen40, seen80, prev_op)] = total
    return total


print(f(5, True, False, None, {}))