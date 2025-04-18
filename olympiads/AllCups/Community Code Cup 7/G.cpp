#include <bits/stdc++.h>
using namespace std;

#define forn(i, l, r) for (int i = l; i < r; ++i)
#define all(a) a.begin(), a.end()
#define f first
#define s second
using ll = long long;
const ll INF = (ll)9e18;

struct DSU {
    vector<int> p, r;
    DSU(int n): p(n), r(n, 0) {
        iota(all(p), 0);
    }
    int find(int x){
        return p[x]==x ? x : p[x]=find(p[x]);
    }
    void unite(int a, int b) {
        a = find(a);
        b = find(b);
        if(a == b) return;
        if(r[a] < r[b]) swap(a,b);
        p[b] = a;
        if(r[a] == r[b]) ++r[a];
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<vector<pair<int,ll>>> g(n);
    vector<tuple<int,int,ll>> E(m);
    forn(i, 0, m){
        int a, b;
        ll w;
        cin >> a >> b >> w;
        --a; --b;
        g[a].push_back(make_pair(b,w));
        g[b].push_back(make_pair(a,w));
        E[i] = make_tuple(a,b,w);
    }

    int k;
    cin >> k;
    vector<int> rad(k);
    forn(i,0,k){
        cin >> rad[i];
        --rad[i];
    }
    vector<ll> dtoradar(n, INF);
    priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<pair<ll,int>>> pq;
    for(int r: rad){
        dtoradar[r] = 0;
        pq.push(make_pair(0LL, r));
    }
    while(!pq.empty()){
        pair<ll,int> top = pq.top(); pq.pop();
        ll d = top.f;
        int u = top.s;
        if(d > dtoradar[u]) continue;
        for(size_t i = 0; i < g[u].size(); ++i){
            int v = g[u][i].f;
            ll w = g[u][i].s;
            if(dtoradar[v] > d + w){
                dtoradar[v] = d + w;
                pq.push(make_pair(dtoradar[v], v));
            }
        }
    }

    struct Edge{ int u, v; ll key; };
    vector<Edge> edges2;
    edges2.reserve(m);
    for(int i = 0; i < m; ++i){
        int u, v; ll w0;
        tie(u, v, w0) = E[i];
        ll key = min(dtoradar[u], dtoradar[v]);
        edges2.push_back({u, v, key});
    }
    sort(all(edges2),
         [](const Edge &A, const Edge &B){ return A.key > B.key; });
    int M = edges2.size();

    int Q;
    cin >> Q;
    vector<int> X(Q), Y(Q), bs;
    vector<ll> ress(Q, 0);
    forn(i, 0, Q){
        cin >> X[i] >> Y[i];
        --X[i]; --Y[i];
        if(X[i] == Y[i]){
            ress[i] = max(0LL, dtoradar[X[i]] - 1);
        } else {
            bs.push_back(i);
        }
    }

    int B = (int)bs.size();
    if(B > 0){
        vector<int> lo(B, 0), hi(B, M - 1), mid(B);
        vector<vector<int>> bucket(M);
        bool any = true;
        while(any){
            any = false;
            forn(e, 0, M) bucket[e].clear();
            forn(b, 0, B) {
                if(lo[b] < hi[b]) {
                    any = true;
                    mid[b] = (lo[b] + hi[b]) >> 1;
                    bucket[mid[b]].push_back(b);
                }
            }
            if(!any) break;

            DSU dsu(n);
            forn(e, 0, M) {
                dsu.unite(edges2[e].u, edges2[e].v);
                for(int b : bucket[e]) {
                    int qi = bs[b];
                    if(dsu.find(X[qi]) == dsu.find(Y[qi]))
                        hi[b] = mid[b];
                    else
                        lo[b] = mid[b] + 1;
                }
            }
        }
        forn(b, 0, B) {
            int qi = bs[b];
            ll w = edges2[lo[b]].key;
            ress[qi] = max(0LL, w - 1);
        }
    }
    forn(i, 0, Q) {
        cout << ress[i] << "\n";
    }
    return 0;
}
