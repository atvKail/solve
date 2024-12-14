n = int(input())

for _ in range(n):
    m = int(input())
    pp = {}

    allu = set()

    for _ in range(m):
        sub = input().strip()
        parts = sub.split(",")
        uid = parts[0].split("-")[-1]
        prbl = parts[1]
        verdict = parts[2]

        if verdict == "OK":
            if uid not in pp:
                pp[uid] = set()
            pp[uid].add(prbl)

        allu.add(sub.split(",")[0].split("-")[-1])

    if pp:
        maxSolved = max(len(prbls) for prbls in pp.values())
        wcnt = sum(1 for prbls in pp.values() if len(prbls) == maxSolved)
    else:
        wcnt = len(allu)

    print(wcnt)
