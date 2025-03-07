def count_programs(start, target, must_include, forbidden):
    dp = [{} for _ in range(target + 1)]
    dp[start][False] = 1

    for x in range(start, target):
        for passed in dp[x]:
            if x in forbidden:
                continue
            for command in [(x + 1), (x + 2), (x * 3)]:
                if command > target:
                    continue
                new_passed = passed or (command == must_include)
                dp[command][new_passed] = dp[command].get(new_passed, 0) + dp[x][passed]

    return dp[target].get(True, 0)


start = 2
target = 18
must_include = 9
forbidden = {16}

result = count_programs(start, target, must_include, forbidden)
print(f"Количество программ: {result}")
