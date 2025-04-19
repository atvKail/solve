#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

#define forn(i, l, r) for(int i = l; i < r; ++i)
#define all(a) a.begin(), a.end()
#define f first
#define s second
using ll = long long;
const int INF = (int)(1e9 + 1);
const int NINF = -INF;

struct SegBeat {
    struct Node { int mx, se, cnt; };
    int n;
    vector<Node> t;

    SegBeat(int _n, int x) : n(_n), t(4 * _n) {
        build(1, 0, n - 1, x);
    }

    void build(int v, int l, int r, int x) {
        if(l == r) {
            t[v] = {x, NINF, 1};
        } else {
            int m = (l + r) >> 1;
            build(v << 1, l, m, x);
            build(v << 1 | 1, m + 1, r, x);
            pull(v);
        }
    }

    void pull(int v) {
        auto &L = t[v << 1], &R = t[v << 1 | 1], &C = t[v];
        if(L.mx > R.mx) {
            C.mx = L.mx;
            C.cnt = L.cnt;
            C.se = max(L.se, R.mx);
        } else if(R.mx > L.mx) {
            C.mx = R.mx;
            C.cnt = R.cnt;
            C.se = max(R.se, L.mx);
        } else {
            C.mx = L.mx;
            C.cnt = L.cnt + R.cnt;
            C.se = max(L.se, R.se);
        }
    }

    void apply_chmin(int v, int x) {
        if(t[v].mx <= x) return;
        t[v].mx = x;
    }

    void push(int v) {
        apply_chmin(v << 1, t[v].mx);
        apply_chmin(v << 1 | 1, t[v].mx);
    }

    void range_chmin(int v, int l, int r, int ql, int qr, int x) {
        if(ql > r || qr < l || t[v].mx <= x) return;
        if(ql <= l && r <= qr && t[v].se < x) {
            apply_chmin(v, x);
            return;
        }
        push(v);
        int m = (l + r) >> 1;
        range_chmin(v << 1, l, m, ql, qr, x);
        range_chmin(v << 1 | 1, m + 1, r, ql, qr, x);
        pull(v);
    }

    int range_max(int v, int l, int r, int ql, int qr) {
        if(ql > r || qr < l) return NINF;
        if(ql <= l && r <= qr) return t[v].mx;
        push(v);
        int m = (l + r) >> 1;
        return max(
            range_max(v << 1, l, m, ql, qr),
            range_max(v << 1 | 1, m + 1, r, ql, qr)
        );
    }

    void range_chmin(int l, int r, int x) {
        range_chmin(1, 0, n - 1, l, r, x);
    }

    int range_max(int l, int r) {
        return range_max(1, 0, n - 1, l, r);
    }
};

struct SegMin {
    int n;
    vector<int> t;

    SegMin(int _n) : n(_n), t(4 * _n, INF) {}

    void build(int v, int l, int r, const vector<int> &a) {
        if(l == r) {
            t[v] = a[l];
        } else {
            int m = (l + r) >> 1;
            build(v << 1, l, m, a);
            build(v << 1 | 1, m + 1, r, a);
            t[v] = min(t[v << 1], t[v << 1 | 1]);
        }
    }

    int query(int v, int l, int r, int ql, int qr) {
        if(ql > r || qr < l) return INF;
        if(ql <= l && r <= qr) return t[v];
        int m = (l + r) >> 1;
        return min(
            query(v << 1, l, m, ql, qr),
            query(v << 1 | 1, m + 1, r, ql, qr)
        );
    }

    int query(int l, int r) {
        return query(1, 0, n - 1, l, r);
    }
};

struct SegMax {
    int n;
    vector<int> t;

    SegMax(int _n) : n(_n), t(4 * _n, NINF) {}

    void build(int v, int l, int r, const vector<int> &a) {
        if(l == r) {
            t[v] = a[l];
        } else {
            int m = (l + r) >> 1;
            build(v << 1, l, m, a);
            build(v << 1 | 1, m + 1, r, a);
            t[v] = max(t[v << 1], t[v << 1 | 1]);
        }
    }

    int query(int v, int l, int r, int ql, int qr) {
        if(ql > r || qr < l) return NINF;
        if(ql <= l && r <= qr) return t[v];
        int m = (l + r) >> 1;
        return max(
            query(v << 1, l, m, ql, qr),
            query(v << 1 | 1, m + 1, r, ql, qr)
        );
    }

    int query(int l, int r) {
        return query(1, 0, n - 1, l, r);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--) {
        int n, m;
        cin >> n >> m;

        vector<int> x(m + 1), a(m + 1), b(m + 1);
        forn(i, 1, m + 1) {
            cin >> x[i] >> a[i] >> b[i];
            --a[i];
            --b[i];
        }

        vector<int> badR(m + 1, m + 1), badL(m + 1, 0);

        {
            SegBeat segR(n, INF);
            for(int i = m; i >= 1; --i) {
                if(x[i] == 0) {
                    segR.range_chmin(a[i], b[i], i);
                } else {
                    int mx = segR.range_max(a[i], b[i]);
                    if(mx < INF) badR[i] = mx;
                }
            }
        }

        {
            SegBeat segL(n, INF);
            for(int i = 1; i <= m; ++i) {
                if(x[i] == 0) {
                    segL.range_chmin(a[i], b[i], -i);
                } else {
                    int mx = segL.range_max(a[i], b[i]);
                    if(mx < INF) badL[i] = -mx;
                }
            }
        }

        vector<int> arrR(m), arrL(m);
        forn(i, 0, m) {
            arrR[i] = badR[i + 1];
            arrL[i] = badL[i + 1];
        }

        SegMin segMinR(m);
        segMinR.build(1, 0, m - 1, arrR);

        SegMax segMaxL(m);
        segMaxL.build(1, 0, m - 1, arrL);

        int q;
        cin >> q;
        while(q--) {
            int l, r;
            cin >> l >> r;
            --l;
            --r;
            bool invR = (segMinR.query(l, r) <= r + 1);
            bool invL = (segMaxL.query(l, r) >= l + 1);
            cout << ((invR || invL) ? "NO\n" : "YES\n");
        }
    }
    return 0;
}

// WA 2 pretest
