#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

#define forn(n) for(int i = 0; i < n; i++)
using ll = long long;
using ld = long int;

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

    public:
    vector<int> tree;
    SegmentTree(const vector<int> &InArr){
        n = InArr.size();
        arr = InArr;
        tree.resize(4 * n + 1);
        build(0, 0, n - 1);
    }

    void build(int v, int l, int r) {
        if (r == l)
            tree[v] = arr[l];
        else {
            int tm = (r + l) / 2;
            build(v*2 + 1, l, tm);
            build(v*2 + 2, tm + 1, r);
            tree[v] = tree[v*2 + 1] + tree[v*2 + 2];
        }
    }

    void update(int v, int l, int r, int pos, int x) {
        if (r == l)
            tree[v] = x;
        else {
            ll tm = (r + l) / 2;
            if (pos <= tm)
                update(v*2 + 1, l, tm, pos, x);
            else
                update(v*2 + 2, tm + 1, r, pos, x);
            tree[v] = tree[v*2 + 1] + tree[v*2 + 2];
        }
    }

    int query(int v, int tl, int tr, int l, int r) {
        if (l > r){
            return 0;
        }
        if (tl == l && tr == r)
            return tree[v];
        int tm = (tl + tr) / 2;
        int lson = query(v * 2 + 1, tl, tm, l, min(tm, r));
        int rson = query(v * 2 + 2, tm + 1, tr, max(tm + 1, l), r);
        return lson + rson;
    }
    
};

int main(){
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int n = 5;
    vector<int> arr{1, 2, 3, 4, 5};
    
    SegmentTree seg(arr);
    
    for (int i = 0; i < n; i++){
        cout << i << " " << seg.query(0, 0, n - 1, 0, i) << endl;
    }

    return 0;
}
