divisor = 25641
divisor2 = 3489
max_n = 10**11

results = []

# Случай 1: x = 0 (маска становится: 4 A 78 82 B 1, всего 8 цифр)
for A in range(10):
    for B in range(10):
        s = f"4{A}7882{B}1"
        n = int(s)
        if n <= max_n and n % divisor == 0:
            results.append((n, n // divisor2))

# Случай 2: x = 2 (маска: 4 A 78 XX 82 B 1, всего 10 цифр)
for A in range(10):
    for x in range(100):
        for B in range(10):
            s = f"4{A}78{x:02d}82{B}1"
            n = int(s)
            if n <= max_n and n % divisor == 0:
                results.append((n, n // divisor2))

# Случай 3: x = 3 (маска: 4 A 78 XXX 82 B 1, всего 11 цифр)
for A in range(10):
    for x in range(1000):
        for B in range(10):
            s = f"4{A}78{x:03d}82{B}1"
            n = int(s)
            if n <= max_n and n % divisor == 0:
                results.append((n, n // divisor2))

results.sort(key=lambda tup: tup[0])

for num, quotient in results:
    print(num, quotient)
