def solve(filename):
    MAX_VAL = 10000  # Решето Эратосфена
    is_prime = [True] * (MAX_VAL + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(MAX_VAL**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, MAX_VAL + 1, i):
                is_prime[j] = False

    with open(filename, "r") as f:
        n = int(f.readline())

        prefix_sum = 0
        prime_count = 0
        best = 0

        min_prefix = {0: 0, 1: None, 2: None}

        for _ in range(n):
            num = int(f.readline())
            prefix_sum += num
            if is_prime[num]:
                prime_count += 1
            r = prime_count % 3

            if min_prefix[r] is not None:
                candidate = prefix_sum - min_prefix[r]
                if candidate > best:
                    best = candidate

            if min_prefix[r] is None:
                min_prefix[r] = prefix_sum

        return best


if __name__ == "__main__":
    files = [
        "USE\\25\\решение заданий фоксфорд\\data\\2\\27_A.txt",
        "USE\\25\\решение заданий фоксфорд\\data\\2\\27_B.txt",
    ]
    answer = [solve(file) for file in files]
    print(*answer)
