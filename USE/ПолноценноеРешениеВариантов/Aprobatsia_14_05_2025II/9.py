cnt = 0
with open(file="USE\\ПолноценноеРешениеВариантов\\Aprobatsia_14_05_2025II\\9.csv", mode="r", encoding="utf-8") as f:
    input = f.readline
    while (x:=input()) != '':
        a = list(map(int, x.split('.')))
        if len(a) == len(set(a)):
            a = set(a)
            m1 = max(a)
            m2 = max(a - {m1})
            if m1 + m2 >= sum(a - {m2} - {m1}):
                cnt += 1
print(cnt)
