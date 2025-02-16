def min_distance_to_photograph(n, x0, segments):
    left, right = 0, 1000
    for a, b in segments:
        left = max(left, min(a, b))
        right = min(right, max(a, b))

    if left > right:
        return -1

    if left <= x0 <= right:
        return 0
    return min(abs(x0 - left), abs(x0 - right))


n, x0 = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(n)]

print(min_distance_to_photograph(n, x0, segments))
