import re


with open("USE\\ПолноценноеРешениеВариантов\\Aprobatsia_14_05_2025I\\24.txt", "r") as f:
    s = f.read().strip()

pattern = re.compile(r"[0-9A-B]+")
odddg = set(["1", "3", "5", "7", "9", "B"])

order = {ch: i for i, ch in enumerate(list("0123456789AB"))}

bst = None
bsti = -1

for mtch in pattern.finditer(s):
    token = mtch.group(0)

    if token[-1] not in odddg:
        continue

    if bst is None:
        bst = token
        bsti = mtch.start()
        continue

    if len(token) > len(bst):
        bst, bsti = token, mtch.start()
    elif len(token) == len(bst):
        for a, b in zip(token, bst):
            if order[a] > order[b]:
                bst, bsti = token, mtch.start()
                break
            elif order[a] < order[b]:
                break
print(bsti)
