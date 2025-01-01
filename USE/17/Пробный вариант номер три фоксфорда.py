numbers = []
with open("USE/17/17.txt", 'r') as f:
    while (x := f.readline()) != '':
        numbers.append(int(x.replace('\n', '')))

min_el = min(numbers, key=lambda x: x if abs(x) % 10 == 3 else 10001)

cnt = 0
max_amount_squared = -10001

for idx1 in range(len(numbers)):
    for idx2 in range(idx1 + 1, len(numbers)):
        x1 = numbers[idx1]
        x2 = numbers[idx2]
        if (m := (x2 + x1) ** 2) >= min_el and (abs(x1) % 10 == 3 or abs(x2) % 10 == 3):
            if abs(x1) % 10 == 3 and abs(x2) % 10 == 3:
                continue
            max_amount_squared = max(max_amount_squared, m)
            cnt += 1
print(cnt, max_amount_squared)

# Неверно, p.s. читать надо нормально, а еще дают свои определения, а не устоявшиеся
# вот верное по мнению составителей:

with open('17.txt') as fin:
    a = [int(i) for i in fin.readlines()]
 
# находим минимальное число, оканчивающееся на 3
# нужно учесть, что в python остаток от деления неотрицательный,
# поэтому числа берем по модулю
 
mn = 10000
for i in a:
    if abs(i) % 10 == 3:
        mn = min(mn, i)
 
cnt = 0
mxsum = 0
 
# перебираем пары, t - кол-во элементов в паре, оканчивающихся на 3
 
for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    t = 0
    if abs(x) % 10 == 3:
        t += 1
    if abs(y) % 10 == 3:
        t += 1
    if t == 1 and (x + y) ** 2 >= abs(mn):
        cnt += 1
        mxsum = max(mxsum, (x + y) ** 2)
 
print(cnt, mxsum)


# ...  оканчивающегося на 3. В ответе запишите два числа: 
# сначала количество найденных пар, затем, через пробел, 
# максимальный из квадратов сумм элементов таких пар. 
# !!!!!В данной задаче под парой подразумевается два идущих подряд элемента последовательности. !!!!!