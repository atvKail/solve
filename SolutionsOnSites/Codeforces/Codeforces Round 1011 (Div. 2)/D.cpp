#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

#define forn(l, n) for(int i = l; i < n; i++)
using ll = long long;
using ld = long int;
const ll NEG = -LLONG_MAX/4;

class SegmentTree {
    private:
        int n;
        vector<ll> arr;
    public:
        vector<ll> tree;
    SegmentTree(const vector<ll> &InArr) {
        n = InArr.size();
        arr = InArr;
        tree.resize(4 * n + 1, NEG);
        build(0, 0, n - 1);
    }

    void build(int v, int l, int r) {
        if(l == r)
            tree[v] = arr[l];
        else {
            int mid = (l + r) / 2;
            build(v * 2 + 1, l, mid);
            build(v * 2 + 2, mid + 1, r);
            tree[v] = max(tree[v * 2 + 1], tree[v * 2 + 2]);
        }
    }

    void update(int v, int l, int r, int pos, ll x) {
        if(l == r)
            tree[v] = x;
        else {
            int mid = (l + r) / 2;
            if(pos <= mid)
                update(v * 2 + 1, l, mid, pos, x);
            else
                update(v * 2 + 2, mid + 1, r, pos, x);
            tree[v] = max(tree[v * 2 + 1], tree[v * 2 + 2]);
        }
    }

    ll query(int v, int tl, int tr, int ql, int qr) {
        if(ql > tr || qr < tl)
            return NEG;
        if(ql <= tl && tr <= qr)
            return tree[v];
        int mid = (tl + tr) / 2;
        return max(query(v * 2 + 1, tl, mid, ql, min(qr, mid)),
                   query(v * 2 + 2, mid + 1, tr, max(ql, mid + 1), qr));
    }
};

 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;
        vector<ll> d(n+1);
        forn (1, n + 1){
            cin >> d[i];
        }

        int M = n / (k + 1);
        vector<ll> prevDP(n + 2, 0), curDP(n + 2, NEG);
        forn (1, n + 2){
            prevDP[i] = 0;
        }

        ll ans = 0;
        for (int x = 1; x <= M; x++){
            int U = n - (x * (k + 1) - 1);
            if(U < 1) break;
            int segSize = U;
            vector<ll> A(segSize, NEG);
            for (int j = 1; j < segSize + 1; j++){
                A[j - 1] = d[j] + prevDP[j + 1];
            }
            SegmentTree segTree(A);
 
            for (int pos = U; pos >= 1; pos--){
                ll best = segTree.query(0, 0, segSize - 1, pos - 1, segSize - 1);
                curDP[pos] = best;
            }
            for (int pos = U + 1; pos <= n + 1; pos++){
                curDP[pos] = NEG;
            }
            ans = max(ans, curDP[1]);
            prevDP = curDP;
        }
        cout << ans << "\n";
    }
    return 0;
}

// Превышено ограничение времени на тесте 4