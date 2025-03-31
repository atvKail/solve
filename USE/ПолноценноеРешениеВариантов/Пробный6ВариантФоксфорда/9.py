cnt = 0
with open("USE\\ПолноценноеРешениеВариантов\\Пробный6ВариантФоксфорда\\9.csv", "r") as f:
    line = f.readline()
    while line != '':
        nums = list(map(int, line.strip().split(';')))
        if len(set(nums)) == 3:
            a = set(nums) - set([i if nums.count(i) == 1 else -1 for i in set(nums)])
            avg = sum(set(nums) - a) / 2
            if avg < a.pop():
                cnt += 1
        line = f.readline()
print(cnt)
