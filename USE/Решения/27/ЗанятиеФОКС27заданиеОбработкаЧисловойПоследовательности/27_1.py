"""
cat "USE\Решения\27\ЗанятиеФОКС27заданиеОбработкаЧисловойПоследовательности\data\27a.txt" | python "USE\Решения\27\ЗанятиеФОКС27заданиеОбработкаЧисловойПоследовательности\27_1.py"
"""

from bisect import bisect_right
import sys


input = sys.stdin.readline
data = []

n = int(input().strip())
prefix = [0] * (n + 1)
for idx in range(n):
    x = int(input().strip())
    prefix[idx + 1] = prefix[idx] + x


min_capacity = float("inf")
min_distance = float("inf")


for S1 in range(prefix[-1] // 2, prefix[-1] + 1):
    S2 = prefix[-1] - S1

    D1 = bisect_right(prefix, S1)
    D2 = bisect_right(prefix, S2)

    if D1 is not None and D2 is not None:
        capacity = max(S1, S2)
        distance = max(D1, D2)

        if capacity < min_capacity or (
            capacity == min_capacity and distance < min_distance
        ):
            min_capacity = capacity
            min_distance = distance

print(min_capacity, min_distance)


# Неверно для файла B
"""
Решение для файла B состовителей:

with open('27b.txt') as F:
  N = int(F.readline())
  data = [ int(F.readline()) for _ in range(N) ]
 
total = sum(data)
half = total / 2
minCapacity, bestWay = None, None
data += data
 
def refreshResults():
  global pos, sumA, minCapacity, bestWay
  curCapacity = max( sumA, total-sumA )
  if sumA > total-sumA:
    stepBackCapacity = max( sumA-data[pos], total-sumA+data[pos] )
    if stepBackCapacity < curCapacity:
      curCapacity = stepBackCapacity
      sumA -= data[pos]
      pos -= 1
  curWay = min( [ pos-startPos, N-2-(pos-startPos) ] )
  if minCapacity == None or curCapacity < minCapacity or\
     (curCapacity == minCapacity and curWay < bestWay):
    minCapacity = curCapacity
    bestWay = curWay
 
startPos = 0
pos, sumA = startPos-1, 0
while sumA < half:
  pos += 1
  sumA += data[pos]
refreshResults()
 
for startPos in range(1,N):
  sumA -= data[startPos-1]
  while sumA < half:
    pos += 1
    sumA += data[pos]
  refreshResults()
 
print( bestWay )
"""