operations = [lambda x: x + 1, lambda x: x + 4, lambda x: x * 3]


print("Задача 19:")


def f(a, n):
    if a >= 64 and n == 3:
        return True
    elif a < 64 and n == 3:
        return False
    elif a >= 64 and n < 3:
        return False
    else:
        if n % 2 == 0:
            return any([f(op(a), n + 1) for op in operations])
        else:
            return all([f(op(a), n + 1) for op in operations])


for s in range(1, 64):
    if f(s, 1):
        print(s)


print("Задача 20:")


def g(a, n):
    if a >= 64 and n == 4:
        return True
    elif a < 64 and n == 4:
        return False
    elif a >= 64 and n < 4:
        return False
    else:
        if n % 2 != 0:
            return any([g(op(a), n + 1) for op in operations])
        else:
            return all([g(op(a), n + 1) for op in operations])


cnt = 0
for s in range(1, 64):
    if g(s, 1) and cnt < 2:
        print(s)
        cnt += 1


print("21 задача:")


def w(a, n):
    if a >= 64 and (n == 3 or n == 5):
        return True
    elif a < 64 and n == 5:
        return False
    elif a >= 64 and n < 5:
        return False
    else:
        if n % 2 == 0:
            return any([w(op(a), n + 1) for op in operations])
        else:
            return all([w(op(a), n + 1) for op in operations])


def z(a, n):
    if a >= 64 and (n == 3):
        return True
    elif a < 64 and n == 3:
        return False
    elif a >= 64 and n < 3:
        return False
    else:
        if n % 2 == 0:
            return any([z(op(a), n + 1) for op in operations])
        else:
            return all([z(op(a), n + 1) for op in operations])


ress = set()
for s in range(1, 64):
    if w(s, 1):
        ress.add(s)

# Исключаем лишнее
for s in range(1, 64):
    if z(s, 1):
        ress -= {s}
print(min(ress))
