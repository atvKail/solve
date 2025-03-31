file = (
    "USE\\ПолноценноеРешениеВариантов\\Пробный6ВариантФоксфорда\\EGE-inf-26-file5.txt"
)

with open(file, "r") as f:
    data = f.read().split()
S = int(data[0])
N = int(data[1])
files = list(map(int, data[2 : 2 + N]))

files.sort()

total = 0
count = 0

for f in files:
    if total + f <= S:
        total += f
        count += 1
    else:
        break

if count == 0:
    print("0 0")
else:
    chosen_max = files[count - 1]

    reserve = S - total
    T = chosen_max + reserve

    max_file = 0
    for f in files:
        if f <= T:
            max_file = f

    print(count, max_file)
