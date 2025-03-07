maxn = -1
for n in range(1000, 5000):
    s = '=' + 51 * '3' + '4' * n + '5' * 53
    while "=3" in s or "=4" in s or "=5" in s:
        if "=3" in s:
            s = s.replace("=3", '55=', 1)
        if "=4" in s:
            s = s.replace("=4", "4=", 1)
        if "=5" in s:
            s = s.replace("=5", "3=", 1)
    if 999 < (sum(map(int, list(s.replace('=', '0'))))) < 10000:
        maxn = max(maxn, n)
print(maxn)