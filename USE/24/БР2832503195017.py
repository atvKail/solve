file_path = "USE\\24\\БР2832503195017.txt"

with open(file_path, 'r') as file:
    s = file.read().strip()

ml = 0
cl = 0
fecnt = 0

for i in range(len(s) - 1):
    cl += 1
    if s[i] == 'F' and s[i + 1] == 'E':
        fecnt += 1

    if fecnt > 200:
        while fecnt > 200:
            if s[i - cl + 1] == 'F' and s[i - cl + 2] == 'E':
                fecnt -= 1
            cl -= 1

    if fecnt == 200:
        ml = max(ml, cl)

print(ml + 1)
