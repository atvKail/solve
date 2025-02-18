from itertools import permutations

# Фрагмент таблицы: список кортежей (значения_столбцов, значение_F)
# Здесь -1 означает «неизвестно, может быть 0 или 1».
rows = [
    ([-1, 1, -1, 0], 0),
    ([-1, 0, 1, -1], 0),
    ([1, -1, 0, -1], 0),
]


def F(x, y, z, w):
    return (not y or z) or not y or not (not x or w)


def generate_replacements(vals):
    if not vals:
        yield []
        return
    head, *tail = vals
    if head == -1:
        for bit in [0, 1]:
            for rest in generate_replacements(tail):
                yield [bit] + rest
    else:
        for rest in generate_replacements(tail):
            yield [head] + rest


variables = ["x", "y", "z", "w"]

found_any = False

for perm in permutations(variables):
    all_match = True
    for vals, f_val in rows:
        row_satisfied = False
        for possible_vals in generate_replacements(vals):
            assignment = dict(zip(perm, possible_vals))
            F_calc = F(
                assignment["x"], assignment["y"], assignment["z"], assignment["w"]
            )

            if F_calc == f_val:
                row_satisfied = True
                break

        if not row_satisfied:
            all_match = False
            break

    if all_match:
        print("".join(perm))
        found_any = True

if not found_any:
    print("Нет подходящих перестановок.")
# Корявый перебор немного, но второй ответ подходит
