n = int(input())
alc = list(map(int, input().split()))
bob = list(map(int, input().split()))

alcCnt = {}
bobCnt = {}

for num in alc:
    if num in alcCnt:
        alcCnt[num] += 1
    else:
        alcCnt[num] = 1

for num in bob:
    if num in bobCnt:
        bobCnt[num] += 1
    else:
        bobCnt[num] = 1

if alcCnt == bobCnt:
    print(0)
else:
    dab = {}
    dba = {}

    for num in set(alcCnt.keys()).union(bobCnt.keys()):
        diff = alcCnt.get(num, 0) - bobCnt.get(num, 0)
        if diff > 0:
            dab[num] = diff
        elif diff < 0:
            dba[num] = -diff

    if len(dab) != 1 or len(dba) != 1:
        print(-1)
    else:
        a = list(dab.keys())[0]
        b = list(dba.keys())[0]

        if dab[a] == dba[b]:
            for i in range(n):
                if alc[i] == a:
                    alc[i] = b
                elif alc[i] == b:
                    alc[i] = a

            if sorted(alc) == sorted(bob):
                print(1)
            else:
                print(-1)
        else:
            print(-1)
