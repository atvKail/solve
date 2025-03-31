with open("USE\\ПолноценноеРешениеВариантов\\Пробный6ВариантФоксфорда\\17_380653.txt", "r") as f:
    input = f.readline

    line = input().strip()
    sums = 0
    while line != '':
        if line[-1] in ['3', '8']:
            sums += int(line)
        line = input().strip()
print(sums)
