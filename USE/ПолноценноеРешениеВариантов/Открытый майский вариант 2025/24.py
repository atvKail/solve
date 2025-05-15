with open("USE\\ПолноценноеРешениеВариантов\\Открытый майский вариант 2025\\24_21908.txt", 'r') as f:
    s = f.readline()
    
valid = set('0123456789ABCD')
even14 = set('02468AC')

best = ''
curr = []
leven = -1

def consider():
    global best
    if leven >= 0:
        cand = ''.join(curr[:leven + 1])
        if len(cand) > len(best) or (len(cand) == len(best) and cand > best):
            best = cand

for c in s:
    if c in valid:
        curr.append(c)
        if c in even14:
            leven = len(curr) - 1
    else:
        consider()
        curr.clear()
        leven = -1
consider()
print(len(best) - 1)
