def dp(value: int, saw14: bool) -> int:
    if value == 9 or value > 26:
        return 0
    saw14 = saw14 or (value == 14)
    if value == 26:
        return 1 if saw14 else 0
    return dp(value + 1, saw14) + dp(value * 2, saw14) + dp(value * 3, saw14)


result = dp(1, False)
print(result)
