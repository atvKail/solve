from itertools import product, permutations


def f(x: bool, y: bool, w: bool, z: bool) -> bool:
    return (not x or z) and not (not w or y) and not y


def main():
    valid_mappings = set()
    for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
        matrix = [(1, 1, 1, x1), (x2, 1, 1, x3), (x4, 1, x5, x6)]
        if len(matrix) == len(set(matrix)):
            for perm in permutations("xywz"):
                if all(f(**dict(zip(perm, row))) for row in matrix):
                    valid_mappings.add("".join(perm))

    if len(valid_mappings) == 1:
        print("Вариант:", valid_mappings.pop())
    elif len(valid_mappings) > 1:
        print("Варианты:", valid_mappings)
    else:
        print("Не найдено!")


if __name__ == "__main__":
    main()
