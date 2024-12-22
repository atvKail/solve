t, p = map(int, input().split())
results = [input().split() for _ in range(t)]
tsksets = [set() for _ in range(p)]

for tid, result in enumerate(results):
    for tskid, sts in enumerate(result):
        if sts == "+":
            tsksets[tskid].add(tid)

seen = set()
for tskset in tsksets:
    tskst = tuple(sorted(tskset))
    if tskst in seen:
        print(0)
        break
    seen.add(tskst)
else:
    print(1)
