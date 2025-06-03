dp = [0] * 2028
for n in range(2025, 2027):
    dp[n] = n
for n in range(2024, 76, -1):
    dp[n] = n * 2 + dp[n + 2]
print(dp[78] - dp[77])
