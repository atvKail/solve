#include <iostream>
#include <vector>
#include <cmath>
#include <unordered_map>
#include <limits>
#include <utility>

using namespace std;

struct Point {
    double x, y;
};

struct UnionFind {
    vector<int> parent;
    vector<int> rank;
    UnionFind(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; i++)
            parent[i] = i;
    }
    int find(int a) {
        if (parent[a] != a)
            parent[a] = find(parent[a]);
        return parent[a];
    }
    void unionSets(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b)
            return;
        if (rank[a] < rank[b])
            swap(a, b);
        parent[b] = a;
        if (rank[a] == rank[b])
            rank[a]++;
    }
};

struct PairHash {
    size_t operator()(const pair<int,int>& p) const {
         
        auto h1 = std::hash<int>()(p.first);
        auto h2 = std::hash<int>()(p.second);
        return h1 ^ (h2 + 0x9e3779b97f4a7c15ULL + (h1 << 6) + (h1 >> 2));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<Point> stars;
    double x, y;
    while (cin >> x >> y) {
        stars.push_back({x, y});
    }
    int n = stars.size();
    if(n == 0)
        return 0;

    UnionFind uf(n);

    unordered_map<pair<int,int>, vector<int>, PairHash> grid;
    for (int i = 0; i < n; i++) {
         
        int cx = static_cast<int>(floor(stars[i].x));
        int cy = static_cast<int>(floor(stars[i].y));
        grid[{cx, cy}].push_back(i);
    }

    for (int i = 0; i < n; i++) {
        int cx = static_cast<int>(floor(stars[i].x));
        int cy = static_cast<int>(floor(stars[i].y));
         
        for (int dx = -1; dx <= 1; dx++) {
            for (int dy = -1; dy <= 1; dy++) {
                pair<int,int> cell = {cx + dx, cy + dy};
                if (grid.find(cell) != grid.end()) {
                    for (int j : grid[cell]) {
                         
                        if (j > i) {
                            double dxVal = stars[i].x - stars[j].x;
                            double dyVal = stars[i].y - stars[j].y;
                            double dist2 = dxVal * dxVal + dyVal * dyVal;
                            if (dist2 <= 1.0 + 1e-9) {  
                                uf.unionSets(i, j);
                            }
                        }
                    }
                }
            }
        }
    }
 
    unordered_map<int, vector<int>> clusters;
    for (int i = 0; i < n; i++) {
        int root = uf.find(i);
        clusters[root].push_back(i);
    }

    vector<Point> centroids;
    for (const auto &entry : clusters) {
        const vector<int> &component = entry.second;
        if (component.size() < 30)
            continue;  
        double bestSum = numeric_limits<double>::infinity();
        int bestIndex = -1;
         
        for (int idx : component) {
            double sumDist = 0.0;
            for (int jdx : component) {
                if (idx == jdx)
                    continue;
                double dxVal = stars[idx].x - stars[jdx].x;
                double dyVal = stars[idx].y - stars[jdx].y;
                sumDist += sqrt(dxVal * dxVal + dyVal * dyVal);
                 
                if (sumDist > bestSum)
                    break;
            }
            if (sumDist < bestSum) {
                bestSum = sumDist;
                bestIndex = idx;
            }
        }
        if (bestIndex != -1)
            centroids.push_back(stars[bestIndex]);
    }

    if (centroids.empty()) {
        cout << "0 0\n";
        return 0;
    }

    double sumX = 0.0, sumY = 0.0;
    for (const auto &p : centroids) {
        sumX += p.x;
        sumY += p.y;
    }
    double avgX = sumX / centroids.size();
    double avgY = sumY / centroids.size();

    long long outX = static_cast<long long>(avgX * 100000);
    long long outY = static_cast<long long>(avgY * 100000);
    cout << outX << " " << outY << "\n";

    return 0;
}
