#include <bits\stdc++.h>

using namespace std;

class Graph {
    int numVertices;
    vector<list<int>> adjLists; // Use vector for better memory management
    vector<bool> visited; // Use vector instead of raw pointer

public:
    Graph(int V);
    void addEdge(int src, int dest);
    void DFS(int vertex);
    void DFS_WithoutRecursion(int vertex);
    void BFS(int startVertex);
    void ClearVisited();
};

Graph::Graph(int vertices) : numVertices(vertices), adjLists(vertices), visited(vertices, false) {}

void Graph::ClearVisited() {
    fill(visited.begin(), visited.end(), false);
}

void Graph::addEdge(int src, int dest) {
    adjLists[src].push_back(dest); // Use push_back for better performance in most cases
}

void Graph::DFS(int vertex) {
    visited[vertex] = true;
    cout << vertex << " ";

    for (int neighbor : adjLists[vertex]) {
        if (!visited[neighbor]) {
            DFS(neighbor);
        }
    }
}

void Graph::DFS_WithoutRecursion(int vertex) {
    stack<int> stack;
    stack.push(vertex);

    while (!stack.empty()) {
        int current = stack.top();
        stack.pop();

        if (!visited[current]) {
            cout << current << " ";
            visited[current] = true;
        }

        for (int neighbor : adjLists[current]) {
            if (!visited[neighbor]) {
                stack.push(neighbor);
            }
        }
    }
}


void Graph::BFS(int startVertex) {
    fill(visited.begin(), visited.end(), false); // Reset visited for BFS
    queue<int> q;
    q.push(startVertex);
    visited[startVertex] = true;

    while (!q.empty()) {
        int vertex = q.front();
        q.pop();
        cout << vertex << " ";

        for (int neighbor : adjLists[vertex]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}

class WeightedGraph {
    int numVertices;
    vector<list<pair<int, int>>> adjLists; // Pair for (destination, weight)

public:
    WeightedGraph(int V);
    void addEdge(int src, int dest, int weight);
    void Dijkstra(int startVertex);
};

WeightedGraph::WeightedGraph(int vertices) : numVertices(vertices), adjLists(vertices) {}

void WeightedGraph::addEdge(int src, int dest, int weight) {
    adjLists[src].emplace_back(dest, weight); // Use emplace_back for efficiency
}

void WeightedGraph::Dijkstra(int startVertex) {
    vector<int> distances(numVertices, numeric_limits<int>::max());
    distances[startVertex] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq; // Min-heap
    pq.emplace(0, startVertex); // Distance, Vertex

    while (!pq.empty()) {
        int currentVertex = pq.top().second;
        pq.pop();

        for (const auto& neighbor : adjLists[currentVertex]) {
            int neighborVertex = neighbor.first;
            int weight = neighbor.second;

            if (distances[currentVertex] + weight < distances[neighborVertex]) {
                distances[neighborVertex] = distances[currentVertex] + weight;
                pq.emplace(distances[neighborVertex], neighborVertex);
            }
        }
    }

    // Output the distances
    for (int i = 0; i < numVertices; ++i) {
        cout << "Distance from " << startVertex << " to " << i << " is " << distances[i] << endl;
    }
}

// Example usage
int main() {
    Graph g(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 3);

    cout << "DFS starting from vertex 2:\n";
    g.DFS(2);

    cout << "\nDFS_WithoutRecursion starting from vertex 2:\n";
    g.ClearVisited();
    g.DFS_WithoutRecursion(2);

    cout << "\nBFS starting from vertex 2:\n";
    g.ClearVisited();
    g.BFS(2);

    WeightedGraph wg(4);
    wg.addEdge(0, 1, 1);
    wg.addEdge(0, 2, 4);
    wg.addEdge(1, 2, 2);
    wg.addEdge(1, 3, 5);
    wg.addEdge(2, 3, 1);

    cout << "\nDijkstra's algorithm starting from vertex 0:\n";
    wg.Dijkstra(0);

    return 0;
}