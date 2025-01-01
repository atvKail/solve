with open("USE/26/26.txt", 'r') as f:
    S, N = map(int, f.readline().split())
    fsizes = [int(f.readline()) for _ in range(N)]

fdivisibl_by3 = [size for size in fsizes if size % 3 == 0]

fdivisibl_by3.sort()
fdivisibl_by3 = fdivisibl_by3[10:]

fdivisibl_by3.sort()

ttl_size = 0
count = 0
max_fsize = 0

for size in fdivisibl_by3:
    if ttl_size + size <= S:
        ttl_size += size
        count += 1
        max_fsize = size
    else:
        break

print(count, max_fsize)


# Неверно
# Правильное решение по мнению составителей:
f = open('26.txt')
data = f.readlines()
k=0
l=1
s = data[0].split()
s = int(s[0])
del(data[0])
for i in range(0, len(data)):
    data[i]=int(data[i])
data=sorted(data)
summa = 0
for count in range (0,len(data)):
    if summa + data[count] > s: break
    if data[count] % 3 == 0:
        if k > 10:
            summa += data[count]
            l += 1
        else:
            k += 1
max=data[0]   
for i in range (0,len(data)):
    if summa - data[i] <= s and data[i] %3 == 0:
        itog = data[i]
print(l , itog)