cnt = 0
minproduct = 100000 * 100000 + 1
with open("USE\\ПолноценноеРешениеВариантов\\Aprobatsia_14_05_2025II\\17.txt", "r") as f:
    a = [int(line.strip()) for line in f if line.strip()]

    absmi = min([x for x in a if 1000 <= abs(x) <= 9999 and abs(x) % 100 == 17])
    triple = []
    for i in range(len(a) - 2):
        triple = [int(a[i]), int(a[i + 1]), a[i + 2]]
        mi = min(triple)
        ma = max(triple)
        f = [triple[i] >= 0 for i in range(3)]
        if f[0] == f[1] == f[2] and absmi * absmi < mi * ma:
            minproduct = min(minproduct, mi * ma)
            cnt += 1
print(cnt, minproduct)
