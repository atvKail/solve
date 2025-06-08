def f(s: str) -> str:
    while "12" in s or "322" in s or "222" in s:
        if "12" in s:
            s = s.replace("12", "2", 1)
        if "322" in s:
            s = s.replace("322", "21", 1)
        if "222" in s:
            s = s.replace("222", "3", 1)
    return s


mx = [-1, -1]
for n in range(4, 10000):
    s = '1' + '2' * n
    mx = max(mx, [n, sum(map(int, list(f(s))))], key=lambda x: x[1])
print(mx[0])
