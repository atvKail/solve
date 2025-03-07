def solve(filename):
    with open(filename, "r") as f:
        n = int(f.readline())
        numbers = [int(f.readline()) for _ in range(n)]

    count2 = 0
    count11 = 0
    count22 = 0
    for num in numbers:
        if num % 2 == 0:
            count2 += 1
        if num % 11 == 0:
            count11 += 1
        if num % 22 == 0:
            count22 += 1
    res = (
        count22 * (n - count22)
        + (count22 * (count22 - 1) // 2)
        + ((count2 - count22) * (count11 - count22))
    )
    return res


if __name__ == "__main__":
    for filename in [
        "USE\\25\\решение заданий фоксфорд\\data\\1\\27A.txt",
        "USE\\25\\решение заданий фоксфорд\\data\\1\\27B.txt",
    ]:
        answer = solve(filename)
        print(f"Файл {filename}: {answer}")
