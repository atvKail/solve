def read_data(file: str, mode="r", encoding="utf-8", func_format=lambda x: x) -> list:
    data = []
    with open(file, mode=mode, encoding=encoding) as f:
        for line in f:
            data.append(func_format(line))
    return data


def solve(data: list) -> int:
    n = int(data[0])
    INF = 10**15
    S0 = 0
    differences = []
    idx = 1
    for _ in range(n):
        a, b = map(int, data[idx].split())
        idx += 1
        c = abs(a - b)
        differences.append(c)
        S0 += c

    r0 = (3 * S0) % 5

    dp = [0] + [INF] * 4
    for c in differences:
        new_dp = dp[:]
        for r in range(5):
            new_r = (r + c) % 5
            if dp[r] + c < new_dp[new_r]:
                new_dp[new_r] = dp[r] + c
        dp = new_dp

    ans = S0 - 2 * dp[r0]
    return ans


if __name__ == "__main__":
    files = [
        "USE\\27\\Занятия в цдо\\data\\27-70A.txt",
        "USE\\27\\Занятия в цдо\\data\\27-70B.txt",
    ]
    for idx_solution in range(2):
        data = read_data(files[idx_solution])
        print(solve(data))
