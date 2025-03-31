alph = "0123456789ABCDEFGH"


def d16tod(s16: str) -> int:
    num = 0
    for idx, ch in enumerate(s16):
        num += 16 ** (len(s16) - idx - 1) * alph.find(ch)
    return num


for x in range(16):
    v1 = f"153{alph[x]}4"
    v2 = f"1{alph[x]}325"
    val = d16tod(v1) + d16tod(v2)
    if val % 15 == 0:
        print(val // 15, x)
        break
