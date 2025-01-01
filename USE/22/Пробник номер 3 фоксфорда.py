from collections import defaultdict, deque

# Данные из таблицы
processes = [
    (1, 4, [0]),
    (2, 10, [1]),
    (3, 18, [0]),
    (4, 18, [1, 2]),
    (5, 14, [3]),
    (6, 13, [3]),
    (7, 19, [2, 5]),
    (8, 12, [4, 7]),
    (9, 7, [4]),
    (10, 10, [9]),
    (11, 14, [1]),
    (12, 8, [0]),
    (13, 15, [5, 6, 9]),
    (14, 6, [11, 12]),
    (15, 15, [7, 8, 13]),
    (16, 12, [13]),
    (17, 9, [14]),
]

# Построение графа зависимостей
graph = defaultdict(list)
indegree = defaultdict(int)  # Счетчик входящих ребер
execution_time = {}  # Время выполнения каждого процесса

for process_id, time, dependencies in processes:
    execution_time[process_id] = time
    for dependency in dependencies:
        if dependency != 0:  # 0 означает, что зависимостей нет
            graph[dependency].append(process_id)
            indegree[process_id] += 1

# Топологическая сортировка (Kahn's Algorithm)
queue = deque([node for node in execution_time if indegree[node] == 0])
total_time = {node: 0 for node in execution_time}

while queue:
    current = queue.popleft()
    total_time[current] += execution_time[current]
    for neighbor in graph[current]:
        indegree[neighbor] -= 1
        total_time[neighbor] = max(total_time[neighbor], total_time[current])
        if indegree[neighbor] == 0:
            queue.append(neighbor)

max_time = max(total_time.values())

print("Минимальное время завершения всех процессов:", max_time)
    