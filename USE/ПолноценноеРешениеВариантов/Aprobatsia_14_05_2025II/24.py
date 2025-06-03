import re


def mbetter(a: str, b: str) -> bool:
    if b is None:
        return True
    if len(a) > len(b):
        return True
    if len(a) < len(b):
        return False
    return a.upper() > b.upper()


with open(
    "USE\\ПолноценноеРешениеВариантов\\Aprobatsia_14_05_2025II\\24.txt", "r"
) as f:
    s = f.readline().strip()

stack = re.findall(r"[0-9A-D]+", s, flags=re.IGNORECASE)
odd14 = set("13579BD")

max14 = None
for chunk in stack:
    lodd = -1
    for i, ch in enumerate(chunk):
        if ch.upper() in odd14:
            lodd = i
    if lodd >= 0:
        cnd = chunk[: lodd + 1]
        if mbetter(cnd, max14):
            max14 = cnd

print(0 if max14 is None else len(max14))
