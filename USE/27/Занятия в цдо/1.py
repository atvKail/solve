def read_data(file: str, mode="r", encoding="utf-8", func_format=lambda x: x) -> list:
    data = []
    with open(file, mode=mode, encoding=encoding) as f:
        for line in f:
            data.append(func_format(line))
    return data


def solve(data: list) -> int:
    n = int(data[0])
    INF = 10**12
    dp = [0] + [INF] * 4
    idx = 1
    for _ in range(n):
        a, b = map(int, data[idx].split())
        idx += 1
        new_dp = [INF] * 5
        for r in range(5):
            if dp[r] != INF:
                new_r = (r + a) % 5
                new_dp[new_r] = min(new_dp[new_r], dp[r] + a)
                new_r = (r + b) % 5
                new_dp[new_r] = min(new_dp[new_r], dp[r] + b)
        dp = new_dp
    return dp[0]


if __name__ == "__main__":
    files = [
        "USE\\27\\Занятия в цдо\\data\\27-5A.txt",
        "USE\\27\\Занятия в цдо\\data\\27-5B.txt",
    ]
    for idx_solution in range(2):
        data = read_data(files[idx_solution])
        print(solve(data))
