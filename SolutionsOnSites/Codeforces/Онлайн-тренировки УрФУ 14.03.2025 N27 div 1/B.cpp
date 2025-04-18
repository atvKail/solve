#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;

#define forn(i, a, b) for (int i = a; i < b; i++)
using ll = long long;

struct SegTree {
    int n;
    vector<ll> seg, lazy;
    SegTree(int n) : n(n) {
        seg.assign(4 * n, 0);
        lazy.assign(4 * n, 0);
    }
    void apply(int v, int l, int r, ll x) {
        seg[v] += x;
        lazy[v] += x;
    }
    void pushDown(int v, int l, int r) {
        if(lazy[v] != 0) {
            int mid = (l + r) / 2;
            apply(v * 2, l, mid, lazy[v]);
            apply(v * 2 + 1, mid + 1, r, lazy[v]);
            lazy[v] = 0;
        }
    }
    void update(int v, int l, int r, int ql, int qr, ll x) {
        if(ql > r || qr < l) return;
        if(ql <= l && r <= qr) {
            apply(v, l, r, x);
            return;
        }
        pushDown(v, l, r);
        int mid = (l + r) / 2;
        update(v * 2, l, mid, ql, qr, x);
        update(v * 2 + 1, mid + 1, r, ql, qr, x);
        seg[v] = min(seg[v * 2], seg[v * 2 + 1]);
    }
    void update(int l, int r, ll x) {
        update(1, 1, n, l, r, x);
    }
    int query(int v, int l, int r) {
        if(l == r) return l;
        pushDown(v, l, r);
        int mid = (l + r) / 2;
        if(seg[v * 2] < 0) return query(v * 2, l, mid);
        else return query(v * 2 + 1, mid + 1, r);
    }
    int query() {
        if(seg[1] >= 0) return -1;
        return query(1, 1, n);
    }
    void reset(int v, int l, int r) {
        if(l == r) {
            seg[v] = lazy[v] = 0;
            return;
        }
        int mid = (l + r) / 2;
        reset(v * 2, l, mid);
        reset(v * 2 + 1, mid + 1, r);
        seg[v] = 0;
        lazy[v] = 0;
    }
    void reset() {
        reset(1, 1, n);
    }
    ll pointQuery(int v, int l, int r, int pos) {
        if(l == r) return seg[v];
        pushDown(v, l, r);
        int mid = (l + r) / 2;
        return pos <= mid ? pointQuery(v * 2, l, mid, pos) : pointQuery(v * 2 + 1, mid + 1, r, pos);
    }
    ll pointQuery(int pos) {
        return pointQuery(1, 1, n, pos);
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<ll> a(n + 1);
        forn(i, 1, n + 1)
            cin >> a[i];
        int q;
        cin >> q;
        vector<tuple<int, int, ll>> ops(q + 1);
        forn(j, 1, q + 1){
            int l, r; ll x;
            cin >> l >> r >> x;
            ops[j] = {l, r, x};
        }

        int jBest = 0;
        SegTree tree(n);
        forn(j, 1, q + 1){
            int l, r; ll x;
            tie(l, r, x) = ops[j];
            tree.update(l, r, x);
            int pos = tree.query();
            if(pos == -1) continue;
            ll d = tree.pointQuery(pos);
            if(d < 0){
                jBest = j;
                tree.reset();
            }
        }

        vector<ll> diff(n + 2, 0), res(n + 1, 0);
        forn(j, 1, jBest + 1){
            int l, r; ll x;
            tie(l, r, x) = ops[j];
            diff[l] += x;
            diff[r + 1] -= x;
        }
        forn(i, 1, n + 1){
            diff[i] += diff[i - 1];
            res[i] = a[i] + diff[i];
        }
        forn(i, 1, n + 1)
            cout << res[i] << " ";
        cout << "\n";
    }
    return 0;
}
