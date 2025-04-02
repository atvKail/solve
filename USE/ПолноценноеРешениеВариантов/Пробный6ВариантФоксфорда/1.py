graph = {
    1: {3: 9, 5: 18, 6: 14, 7: 11},
    2: {3: 5, 4: 12, 6: 7, 7: 8},
    3: {1: 9, 2: 5},
    4: {2: 12, 6: 10},
    5: {1: 18, 7: 15},
    6: {1: 14, 2: 7, 4: 10},
    7: {1: 11, 2: 8, 5: 15},
}


def dijkstra(graph, start, n):
    import heapq

    dists = {i: float("infinity") for i in range(1, n + 1)}
    dists[start] = 0
    pqueue = [(0, start)]

    while pqueue:
        current_distance, cv = heapq.heappop(pqueue)

        if current_distance > dists[cv]:
            continue

        for ngbr, w in graph[cv].items():
            dist = current_distance + w
            if dist < dists[ngbr]:
                dists[ngbr] = dist
                heapq.heappush(pqueue, (dist, ngbr))

    return dists


print(dijkstra(graph, 4, 7))

# Оишбся, было: "7: {1: 11, 2: 8, 5: 14},", а правильно: 7: {1: 11, 2: 8, 5: 15},