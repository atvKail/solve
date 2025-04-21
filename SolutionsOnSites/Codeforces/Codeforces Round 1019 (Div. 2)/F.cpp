#include <iostream>
#include <vector>
#include <map>
using namespace std;

#define forn(i, l, r) for(int i = l; i < r; ++i)
#define all(a) a.begin(), a.end()
#define f first
#define s second
using ll = long long;

const int MAXN = 1e5 + 10;

int a[MAXN];

struct SegmentTree{
    vector<int> tree, lazy;
    int n;

    SegmentTree(int _n) : n(_n), tree(4 * _n, 0), lazy(4 * _n, -1){}

    void push(int v, int tl, int tr){
        if(lazy[v] != -1){
            tree[v] = max(tree[v], lazy[v]);
            if(tl != tr){
                if(lazy[2 * v] == -1) lazy[2 * v] = lazy[v];
                else lazy[2 * v] = max(lazy[2 * v], lazy[v]);
                if(lazy[2 * v + 1] == -1) lazy[2 * v + 1] = lazy[v];
                else lazy[2 * v + 1] = max(lazy[2 * v + 1], lazy[v]);
            }
            lazy[v] = -1;
        }
    }

    void update(int v, int tl, int tr, int l, int r, int val){
        push(v, tl, tr);
        if(tl > r || tr < l) return;
        if(tl >= l && tr <= r){
            tree[v] = max(tree[v], val);
            if(tl != tr){
                if(lazy[2 * v] == -1) lazy[2 * v] = val;
                else lazy[2 * v] = max(lazy[2 * v], val);
                if(lazy[2 * v + 1] == -1) lazy[2 * v + 1] = val;
                else lazy[2 * v + 1] = max(lazy[2 * v + 1], val);
            }
            return;
        }
        int mid = (tl + tr) / 2;
        update(2 * v, tl, mid, l, r, val);
        update(2 * v + 1, mid + 1, tr, l, r, val);
        tree[v] = max(tree[2 * v], tree[2 * v + 1]);
    }

    int query(int v, int tl, int tr, int idx){
        push(v, tl, tr);
        if(tl == tr) return tree[v];
        int mid = (tl + tr) / 2;
        if(idx <= mid) return query(2 * v, tl, mid, idx);
        return query(2 * v + 1, mid + 1, tr, idx);
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--){
        int n, k;
        cin >> n >> k;
        
        forn(i, 1, n + 1) cin >> a[i];

        int mask = (1 << k) - 1;
        SegmentTree st(n);
        map<int, int> dp_prev;

        forn(r, 1, n + 1){
            map<int, int> dp_curr;
            dp_curr[a[r]] = r;

            for(auto it = dp_prev.begin(); it != dp_prev.end(); ++it){
                int u = it->f;
                int l_prev = it->s;
                int v = (~(u | a[r])) & mask;
                if(dp_curr.find(v) == dp_curr.end() || l_prev < dp_curr[v]){
                    dp_curr[v] = l_prev;
                }
            }

            for(auto it = dp_curr.begin(); it != dp_curr.end(); ++it){
                int v = it->f;
                int l = it->s;
                st.update(1, 1, n, l, r, v);
            }
            dp_prev = dp_curr;
        }

        forn(i, 1, n + 1){
            cout << st.query(1, 1, n, i) << " ";
        }
        cout << "\n";
    }
    return 0;
}