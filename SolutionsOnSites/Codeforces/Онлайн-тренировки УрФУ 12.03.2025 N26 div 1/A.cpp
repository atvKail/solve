#include <iostream>
#include <vector>
using namespace std;

#define forn(i, a, b) for (int i = a; i < b; i++)
using ll = long long;

struct Rook {
    ll x, y;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;
    
    vector<vector<Rook>> rooks(n + 1);
    
    forn(i, 1, n + 1) {
        rooks[i].push_back({100LL * i, 100LL * i});
    }
    
    const ll offset = 100000;
    forn(i, 0, m) {
        int u, v;
        cin >> u >> v;
        ll X = offset + i;
        rooks[u].push_back({100LL * u, X});
        rooks[v].push_back({100LL * v, X});
    }
    
    forn(i, 1, n + 1) {
        cout << rooks[i].size() << "\n";
        for (auto& r : rooks[i]) {
            cout << r.x << " " << r.y << "\n";
        }
    }
    
    return 0;
}
