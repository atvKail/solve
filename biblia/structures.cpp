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

class SegmentTree{
private:
    int n;
    vector<int> arr;
    vector<int> tree;

    void build(int v, int tl, int tr) {
        if (tl == tr) {
            tree[v] = arr[tl];
        } else {
            int tm = tl + (tr - tl) / 2;
            build(2 * v, tl, tm);
            build(2 * v + 1, tm + 1, tr);
            tree[v] = tree[2 * v] + tree[2 * v + 1];
        }
    }
public:
    // vector<int> tree;
    SegmentTree(const vector<int> &InputArr){
        n = InputArr.size();
        arr = InputArr;
        tree.resize(4 * n);
        build(1, 0, arr.size() - 1);
    }

    void update(int v, int tl, int tr, int pos, int x){
        tree[v] += x; // Любая операция
        if (tl == tr){
            // tree[v] = x;
            return;
        }
        int tm = tl + (tr - tl) / 2;
        if (pos < tm){
            update(2 * v, tl, tm, pos, x);
        }
        else{
            update(2 * v + 1, tm + 1, tr, pos, x);
        }
        // tree[v] = tree[2 * v] + tree[2 * v + 1];
    }

    int getSum(int v, int tl, int tr, int l, int r){
        if (tl == l && tr == r){
            return tree[v];
        }
        cout << v;
        int result = 0;
        int tm = tl + (tr - tl) / 2;
        if (l <= tm){
            result += getSum(2 * v, tl, tm, l, min(r, tm)); // Любая операция
        }
        if (r > tm){
            result += getSum(2 * v + 1, tm + 1, tr, max(l, tm + 1), r); // Любая операция
        }
        return result;
    }
};
