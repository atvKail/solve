import sys

input = sys.stdin.readline


def ask_triangle(i, j, k):
    print(f"? {i} {j} {k}")
    sys.stdout.flush()

    resp = input().strip()
    if not resp:
        return -1
    val = int(resp)
    return val


def solve(n):
    if n == 3:
        print("! 1 2 3")
        sys.stdout.flush()
        return

    triangle = [1, 2, 3]
    max_queries = 75
    used_queries = 0

    pos = 0
    while used_queries < max_queries:
        i, j, k = triangle
        ans = ask_triangle(i, j, k)
        used_queries += 1

        if ans == -1:
            sys.exit(0)

        if ans == 0:
            print(f"! {i} {j} {k}")
            sys.stdout.flush()
            return
        else:
            triangle[pos] = ans
            pos = (pos + 1) % 3

    i, j, k = triangle
    print(f"! {i} {j} {k}")
    sys.stdout.flush()


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    solve(n)

# Неправильный ответ на тесте 13
