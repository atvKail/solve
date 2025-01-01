def count_programs(start, end, must_include=None, must_exclude=None):
    # DP-массив для подсчета путей
    dp = [0] * (end + 1)
    dp[start] = 1  # Начальное состояние

    # Заполняем DP
    for x in range(start, end + 1):
        if must_exclude and x in must_exclude:
            dp[x] = 0
            continue
        if x - 1 >= start:
            dp[x] += dp[x - 1]
        if x % 2 == 0 and x // 2 >= start:
            dp[x] += dp[x // 2]

    # Если нужно учитывать обязательное включение
    if must_include:
        return dp[must_include], dp[end] - dp[must_include]
    return dp[end]

# 1. Программы из 1 в 14, без числа 22
to_14 = count_programs(1, 14, must_exclude={22})

# 2. Программы из 14 в 54, без числа 22
from_14_to_54 = count_programs(14, 54, must_exclude={22})

result = to_14 * from_14_to_54
print(result)
