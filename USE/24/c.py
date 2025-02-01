a = [x if x.count('O') <= 2 else '*' for x in open('USE/24/sdamgia17463002/24.txt').readline().split('D')[1:-1]]
s = 'D'+'D'.join(a)+'D'
print(max([len(x) for x in s.split('*')]))