def read_data(file: str, mode="r", encoding="utf-8", func_format=lambda x: x) -> list:
    data = []
    with open(file, mode=mode, encoding=encoding) as f:
        for line in f:
            data.append(func_format(line))
    return data


def solve(data: list) -> int:
    n = int(data[0])
    measurements = list(map(int, data[1:]))

    sq = [x * x for x in measurements]

    prefix = [0] * n
    prefix[0] = sq[0]
    for i in range(1, n):
        prefix[i] = min(prefix[i - 1], sq[i])

    ans = float("inf")
    for j in range(5, n):
        candidate = sq[j] + prefix[j - 5]
        if candidate < ans:
            ans = candidate
    return ans


if __name__ == "__main__":
    files = [
        "USE\\27\\Занятия в цдо\\data\\27-8A.txt",
        "USE\\27\\Занятия в цдо\\data\\27-8B.txt",
    ]
    for idx_solution in range(2):
        data = read_data(files[idx_solution])
        print(solve(data))
