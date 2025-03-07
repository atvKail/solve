import itertools


def generate_candidates():
    candidates = []
    for star_len in range(0, 4):
        if star_len == 0:
            star_options = [""]
        else:
            star_options = [
                "".join(t) for t in itertools.product("0123456789", repeat=star_len)
            ]
        for q in "0123456789":
            for star in star_options:
                s = "3" + q + "5919" + star + "7"
                n = int(s)

                candidates.append(n)
    return candidates


def main():
    candidates = generate_candidates()
    valid = []
    for n in candidates:
        if n % 2021 == 0:
            valid.append(n)
    valid.sort()

    count = 0
    for n in valid:
        print(n, n // 2021)
        count += 1
        if count == 3:
            break


if __name__ == "__main__":
    main()
