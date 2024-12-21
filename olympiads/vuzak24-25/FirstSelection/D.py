def min_changes_to_almost_sawtooth(n, b):
    changes_even = 0
    changes_odd = 0

    for i in range(1, n, 2):
        if b[i] >= b[i - 1]:
            changes_even += 1
        if i + 1 < n and b[i] >= b[i + 1]:
            changes_even += 1

    for i in range(0, n, 2):
        if i > 0 and b[i] <= b[i - 1]:
            changes_odd += 1
        if i + 1 < n and b[i] <= b[i + 1]:
            changes_odd += 1

    return min(changes_even, changes_odd)



n = int(input())
b = list(map(int, input().split()))

result = min_changes_to_almost_sawtooth(n, b)

print(result)
