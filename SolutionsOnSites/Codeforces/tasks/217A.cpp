#include <bits/stdc++.h>
using namespace std;

#define forn(i, l, r) for(int i = l; i < r; ++i)
#define all(a) (a).begin(), (a).end()
#define f first
#define s second
#define pb push_back
#define mp make_pair

using ll = long long;
using pii = pair<int, int>;
using vi = vector<int>;
using vb = vector<bool>;
using vvi = vector<vi>;
using unomapss = unordered_map<string, string>;

int n;
vb vis;
vector<pii> pts;

void dfs(int u){
    vis[u] = true;
    forn(v, 0, n){
        if(!vis[v] && (pts[v].f == pts[u].f || pts[v].s == pts[u].s)){
            dfs(v);
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    cin >> n;
    pts.resize(n);
    forn(i, 0, n){
        cin >> pts[i].f >> pts[i].s;
    }

    vis.assign(n, false);
    int cmps = 0;
    forn(i, 0, n){
        if(!vis[i]){
            cmps++;
            dfs(i);
        }
    }

    cout << max(0, cmps - 1) << "\n";
    return 0;
}
