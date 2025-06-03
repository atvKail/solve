def f(s: str) -> str:
    while "19" in s or "399" in s or "999" in s:
        s = s.replace("19", "9", 1)
        s = s.replace("399", "91", 1)
        s = s.replace("999", "3", 1)
    return s


for n in range(1, 100):
    if sum(map(int, list(f('1' + "9" * n)))) == 27:
        print(n)
        break
