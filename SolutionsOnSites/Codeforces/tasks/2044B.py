results = []
for _ in range(int(input())):
    s = input()[::-1]
    results.append(
        "".join(
            [
                ("p" if s[i] == "q" else "q") if s[i] != "w" else "w"
                for i in range(len(s))
            ]
        )
    )
print("\n".join(results))
