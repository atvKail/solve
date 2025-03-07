def count_paths(n, flag, memo):
    if n == 21:
        return 0
    if n == 49:
        return 1 if flag else 0
    if n > 49:
        return 0
    if n == 18:
        flag = True
    key = (n, flag)
    if key in memo:
        return memo[key]
    ways = 0
    if n + 1 <= 49 and (n + 1) != 21:
        ways += count_paths(n + 1, flag or (n + 1 == 18), memo)
    if 2 * n <= 49 and (2 * n) != 21:
        ways += count_paths(2 * n, flag or (2 * n == 18), memo)
    memo[key] = ways
    return ways


def main():
    memo = {}
    ways_from_2 = count_paths(2, False, memo)
    result = 2 * ways_from_2
    print("Количество программ:", result)


if __name__ == "__main__":
    main()
