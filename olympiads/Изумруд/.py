###### task 1
graph = {
    "A": {"B": 3, "C": 8, "E": 4},
    "B": {"A": 3, "C": 5, "D": 9, "E": 2, "F": 13},
    "C": {"A": 8, "B": 5, "D": 4, "E": 3},
    "D": {"B": 9, "C": 4, "E": 3},
    "E": {"A": 4, "B": 2, "C": 3, "D": 3, "F": 11},
    "F": {"B": 13, "E": 11},
}

import heapq


def dijkstra(graph, start, end):
    queue = [(0, start)]
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    visited = set()

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == end:
            return current_distance

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return float("inf")


shortest_path_distance = dijkstra(graph, "A", "F")
print(shortest_path_distance)


###### task 2
s = "7" * 80
while "777" in s or "888" in s:
    if "777" in s:
        s = s.replace("777", "8", 1)
    else:
        s = s.replace("888", "7", 1)
print(s)


####task 3
def find_min_r():
    for n in range(1, 1000):
        binary = bin(n)[2:]
        sum1 = sum(int(digit) for digit in binary)
        binary += str(sum1 % 2)
        sum2 = sum(int(digit) for digit in binary)
        binary += str(sum2 % 2)
        r = int(binary, 2)
        if r > 60:
            return r


result = find_min_r()
print(result)

#####task 4
dp = [0] * 29
dp[2] = 1

for x in range(2, 28):
    if x + 1 <= 28:
        dp[x + 1] += dp[x]
    if x * 3 <= 28:
        dp[x * 3] += dp[x]
print(dp[28])


####task 5
graph = {
    'A': {'B': 2, 'C': 6, 'D': 4},
    'B': {'A': 2, 'C': 2, 'E': 9},
    'C': {'A': 6, 'B': 2, 'D': 1, 'E': 6},
    'D': {'A': 4, 'C': 1},
    'E': {'B': 9, 'C': 6}
}

print(dijkstra(graph, "A", "E"))