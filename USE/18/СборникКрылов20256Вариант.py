def CountingTheLiftingMethod(k):
    N = 33
    operations = [1, 2, k]

    memo = {}

    def f(step):
        if step == N:
            return 1

        if step > N:
            return 0

        if step in memo:
            return memo[step]

        total_ways = 0
        for op in operations:
            total_ways += f(step + op)

        memo[step] = total_ways
        return total_ways

    return f(0)


print(f"{CountingTheLiftingMethod(k=4)} {CountingTheLiftingMethod(k=5)}")
