def read_data(file: str, mode="r", encoding="utf-8", func_format=lambda x: x) -> list:
    data = []
    with open(file, mode=mode, encoding=encoding) as f:
        for line in f:
            data.append(func_format(line))
    return data


def solve(data: list) -> int:
    n = int(data[0][0])
    NEG_INF = -(10**15)
    dp = [NEG_INF] * 16
    dp[0] = 0
    idx = 1
    for _ in range(n):
        a, b = map(int, data[idx])
        idx += 1
        new_dp = [NEG_INF] * 16
        for r in range(16):
            if dp[r] != NEG_INF:
                r1 = (r + a) % 16
                r2 = (r + b) % 16
                new_dp[r1] = max(new_dp[r1], dp[r] + a)
                new_dp[r2] = max(new_dp[r2], dp[r] + b)
        dp = new_dp
    return max(dp[r] for r in range(16) if r != 10)


if __name__ == "__main__":
    files = [
        "USE\\27\\Занятия в цдо\\data\\27-27A.txt",
        "USE\\27\\Занятия в цдо\\data\\27-27B.txt",
    ]
    for idx_solution in range(2):
        data = read_data(files[idx_solution], func_format=lambda x: x.split())
        print(solve(data))
