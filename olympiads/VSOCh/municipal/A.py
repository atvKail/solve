d, m = [int(input()) for _ in range(2)]
print(min(abs(m // d * d + d - m), abs(m - m // d * d)))
