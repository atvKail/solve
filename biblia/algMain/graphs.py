from collections import deque
import heapq
import sys

class Graph:
    def __init__(self, V):
        self.numVertices = V
        self.adjLists = [[] for _ in range(V)]
        self.visited = [False] * V

    def add_edge(self, src, dest):
        self.adjLists[src].append(dest)

    def dfs(self, vertex):
        self.visited[vertex] = True
        print(vertex, end=" ")

        for neighbor in self.adjLists[vertex]:
            if not self.visited[neighbor]:
                self.dfs(neighbor)

    def bfs(self, startVertex):
        self.visited = [False] * self.numVertices
        q = deque([startVertex])
        self.visited[startVertex] = True

        while q:
            vertex = q.popleft()
            print(vertex, end=" ")

            for neighbor in self.adjLists[vertex]:
                if not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    q.append(neighbor)

class WeightedGraph:
    def __init__(self, V):
        self.numVertices = V
        self.adjLists = [[] for _ in range(V)]

    def add_edge(self, src, dest, weight):
        self.adjLists[src].append((dest, weight))

    def dijkstra(self, startVertex):
        distances = [sys.maxsize] * self.numVertices
        distances[startVertex] = 0

        pq = []
        heapq.heappush(pq, (0, startVertex))

        while pq:
            currentDistance, currentVertex = heapq.heappop(pq)

            for neighbor, weight in self.adjLists[currentVertex]:
                if currentDistance + weight < distances[neighbor]:
                    distances[neighbor] = currentDistance + weight
                    heapq.heappush(pq, (distances[neighbor], neighbor))

        for i in range(self.numVertices):
            print(f"Distance from {startVertex} to {i} is {distances[i]}")

# Example usage
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    print("DFS starting from vertex 2:")
    g.dfs(2)
    print("\nBFS starting from vertex 2:")
    g.bfs(2)

    wg = WeightedGraph(4)
    wg.add_edge(0, 1, 1)
    wg.add_edge(0, 2, 4)
    wg.add_edge(1, 2, 2)
    wg.add_edge(1, 3, 5)
    wg.add_edge(2, 3, 1)

    print("\nDijkstra's algorithm starting from vertex 0:")
    wg.dijkstra(0)
