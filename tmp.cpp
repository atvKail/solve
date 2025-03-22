#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

#define forn(n) for(int i = 0; i < n; i++)
using ll = long long;
using ld = long int;

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
        int left_son = query(v*2 + 1, tl, tm, l, min(tm, r));
        int right_son = query(v*2 + 2, tm + 1, tr, max(tm + 1, l), r);
        return left_son + right_son;
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
