#include <iostream>
#include <vector>
#include <tuple>
using namespace std;

#define forn(i, l, r) for(int i = l; i < r; ++i)
#define all(a) (a).begin(), (a).end()
#define f first
#define s second

using ll = long long;

struct Fenwick{
    int n;
    vector<ll> f;
    Fenwick(int _n): n(_n), f(n + 1, 0){}
    void add(int i, ll v){
        for(; i <= n; i += i & -i)
            f[i] += v;
    }
    ll sum(int i) const{
        ll s = 0;
        for(; i > 0; i -= i & -i)
            s += f[i];
        return s;
    }
    void range_add(int l, int r, ll v){
        if(l > r) return;
        add(l, v);
        add(r + 1, -v);
    }
    ll point(int i) const{
        return sum(i);
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    int M = m;

    vector<ll> a(n + 1);
    forn(i, 1, n + 1) cin >> a[i];

    vector<vector<int>> adj(n + 1);
    forn(i, 0, n - 1){
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> tin(n + 1), tout(n + 1), depth(n + 1);
    int timer = 0;

    vector<tuple<int, int, int>> stk;
    stk.emplace_back(1, 0, 0);
    while (!stk.empty()){
        tuple<int, int, int> tp = stk.back();
        int u = get<0>(tp);
        int p = get<1>(tp);
        int st = get<2>(tp);
        stk.pop_back();

        if(st == 0){
            tin[u] = ++timer;
            stk.emplace_back(u, p, 1);
            forn(i, 0, adj[u].size()){
                int v = adj[u][i];
                if(v == p) continue;
                depth[v] = depth[u] + 1;
                stk.emplace_back(v, u, 0);
            }
        } else{
            tout[u] = timer;
        }
    }

    Fenwick B0(n + 2), B1(n + 2);

    forn(q, 0, M){
        int type;
        cin >> type;
        if(type == 1){
            int x; ll val;
            cin >> x >> val;
            int l = tin[x], r = tout[x];
            if(depth[x] % 2 == 0){
                B0.range_add(l, r, +val);
                B1.range_add(l, r, -val);
            } else{
                B0.range_add(l, r, -val);
                B1.range_add(l, r, +val);
            }
        } else{
            int x;
            cin >> x;
            int p = depth[x] % 2;
            ll add = (p == 0 ? B0.point(tin[x]) : B1.point(tin[x]));
            cout << (a[x] + add) << "\n";
        }
    }

    return 0;
}
