def read_data(file: str, mode="r", encoding="utf-8", func_format=lambda x: x) -> list:
    data = []
    with open(file, mode=mode, encoding=encoding) as f:
        for line in f:
            data.append(func_format(line))
    return data


def solve(data: list) -> int:
    n = int(data[0])
    freq = [0] * 1001
    for i in range(1, n + 1):
        num = int(data[i])
        freq[num] += 1

    ans = 0
    for i in range(1, 1001):
        if freq[i] == 0:
            continue
        for j in range(i, 1001):
            if freq[j] == 0:
                continue
            if i == j and freq[i] < 2:
                continue
            product = i * j
            if product % 6 == 0:
                ans = max(ans, product)
    return ans


if __name__ == "__main__":
    files = [
        "USE\\27\\Занятия в цдо\\data\\27-6A.txt",
        "USE\\27\\Занятия в цдо\\data\\27-6B.txt",
    ]
    for idx_solution in range(2):
        data = read_data(files[idx_solution])
        print(solve(data))
