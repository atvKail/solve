def no_adjacent_evens(digits):
    for i in range(len(digits) - 1):
        if digits[i] % 2 == 0 and digits[i + 1] % 2 == 0:
            return False
    return True


even_digits = [0, 2, 4, 6]
odd_digits = [1, 3, 5, 7]


count = 0


for pos in range(5):
    for d1 in range(8):
        if d1 == 0:
            continue
        for d2 in range(8):
            if d2 == 3 and pos != 1:
                continue
            for d3 in range(8):
                if d3 == 3 and pos != 2:
                    continue
                for d4 in range(8):
                    if d4 == 3 and pos != 3:
                        continue
                    for d5 in range(8):
                        if d5 == 3 and pos != 4:
                            continue

                        digits = [d1, d2, d3, d4, d5]

                        if digits.count(3) != 1:
                            continue

                        if no_adjacent_evens(digits):
                            count += 1


print(count)
