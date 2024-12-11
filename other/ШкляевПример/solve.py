import matplotlib.pyplot as plt


def read_stars(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    stars = [list(map(float, line.split())) for line in lines]
    return stars


stars_A = read_stars('27A_18031.txt')
stars_B = read_stars('27B_18031.txt')

x_A, y_A = zip(*stars_A)
x_B, y_B = zip(*stars_B)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(x_A, y_A, color='blue', label='File A')
plt.title('Star Clusters in File A')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(x_B, y_B, color='green', label='File B')
plt.title('Star Clusters in File B')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.legend()

plt.tight_layout()
plt.show()


def f(point, alternation):
    x, y = point
    # Определяем кластер для файла A (task == 0)
    if alternation == 0:
        return int(x + y > 4)
    
    # Определяем кластер для файла B (task == 1)
    if alternation == 1:
        if x > 13:  # Точки с x > 13
            return 0
        elif x > 8:  # Точки с 8 < x <= 13
            if y > 13:
                return 1
            else:
                return 2
        else:  # Точки с x <= 8
            if y > 5:
                return 3
            return 4

def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def read_data(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            x, y = map(float, line.replace(',', '.').split())
            data.append([x, y])
    return data

base = ''
files = ['27A_18031.txt', '27B_18031.txt']
clusters = [2, 5]  # Количество кластеров
mdc = [
    [(0, 1)],  # Для файла A ищем минимальное расстояние между кластерами 0 и 1
    [(1, 2), (2, 3), (3, 4)]
]

for t in range(2):
    all_data = [[] for _ in range(clusters[t])]
    stars = read_data(base + files[t])
    for star in stars:
        all_data[f(star, t)].append(star)
    
    dm = float('inf')
    mp1 = mp2 = None

    for cl in mdc[t]:
        for p1 in all_data[cl[0]]:
            for p2 in all_data[cl[1]]:
                d = dist(p1, p2)
                if d < dm:
                    dm = d
                    mp1 = p1
                    mp2 = p2

    sx = int((mp1[0] + mp2[0]) * 1000)
    sy = int((mp1[1] + mp2[1]) * 1000)
    
    print(sx, sy)

