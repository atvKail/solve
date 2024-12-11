#include <bits\stdc++.h>
using namespace std;
class DSU {
public:
    DSU(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
        }
    }
    int find(int u, int cnt = 0) {
        if (parent[u] != u) {
            parent[u] = find(parent[u]);
        }
        return parent[u];
    }
    void unite(int u, int v) {
        int root_u = find(u);
        int root_v = find(v);
        if (root_u != root_v) {
            if (rank[root_u] < rank[root_v]) {
                parent[root_u] = root_v;
            } else if (rank[root_u] > rank[root_v]) {
                parent[root_v] = root_u;
            } else {
                parent[root_u] = root_v;
                rank[root_v]++;
            }
        }
    }
    std::vector<int> get_parent(){
        return parent;
    }
    std::vector<int> get_rank(){
        return rank;
    }
private:
    std::vector<int> parent;
    std::vector<int> rank;
};


class SegmentTree {
private:
    vector<int> arr;
    vector<int> tree;

    void build(int v, int tl, int tr) {
        if (tl == tr) {
            tree[v] = arr[tl];
        } else {
            int tm = (tl + tr) / 2;
            build(2 * v, tl, tm);
            build(2 * v + 1, tm + 1, tr);
            tree[v] = tree[2 * v] + tree[2 * v + 1];
        }
    }

public:
    SegmentTree(const vector<int>& inputArr) {
        arr = inputArr;
        tree.resize(4 * arr.size());
        build(1, 0, arr.size() - 1);
    }

    int query(int v, int tl, int tr, int l, int r) {
        if (l > r) {
            return 0;
        }
        if (l == tl && r == tr) {
            return tree[v];
        }
        int tm = (tl + tr) / 2;
        return query(2 * v, tl, tm, l, min(r, tm)) + query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r);
    }

    void update(int v, int tl, int tr, int pos, int newVal) {
        if (tl == tr) {
            tree[v] = newVal;
        } else {
            int tm = (tl + tr) / 2;
            if (pos <= tm) {
                update(2 * v, tl, tm, pos, newVal);
            } else {
                update(2 * v + 1, tm + 1, tr, pos, newVal);
            }
            tree[v] = tree[2 * v] + tree[2 * v + 1];
        }
    }
};