file_A = "USE\\ПолноценноеРешениеВариантов\\Пробный6ВариантФоксфорда\\387705_A.txt"


def y1(x):
    return x


def y2(x):
    return x - 3


def y3(x):
    return x - 8


with open(file_A, "r") as f:
    line = f.readline().strip()
    data_A = []
    while line != "":
        data_A.append(list(map(float, line.replace(",", ".").split())))
        line = f.readline()

px, py = 0, 0
clusters = [[], []]
for x, y in data_A:
    if y1(x) < y:
        continue
    elif y3(x) > y:
        continue

    if y2(x) > y:
        clusters[1].append([x, y])
        px += x
        py += y
    else:
        clusters[0].append([x, y])
        px += x
        py += y

m = 1e5
n = len(clusters[0]) + len(clusters[1])
print(int(px / n * m), int(py / n * m))