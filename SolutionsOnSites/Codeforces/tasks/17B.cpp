#include<bits/stdc++.h>
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
using vvi = vector<vi>;

const ll INF = (ll)4e18;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if(!(cin >> n)) return 0;
    vector<ll> q(n + 1);
    forn(i, 1, n + 1){
        cin >> q[i];
    }

    int m;
    cin >> m;    
    vector<ll> cmin(n + 1, INF);
    vector<bool> hincom(n + 1, false);
    forn(i, 0, m){
        int a, b;
        ll c;
        cin >> a >> b >> c;
        if(c < cmin[b]){
            cmin[b] = c;
        }
        hincom[b] = true;
    }
    
    vi noin;
    forn(i, 1, n + 1){
        if(!hincom[i]){
            noin.pb(i);
        }
    }
    if((int)noin.size() != 1){
        cout << -1 << "\n";
        return 0;
    }

    int root = noin[0];
    ll ttl = 0;
    forn(i, 1, n + 1){
        if(i == root) continue;
        if(cmin[i] == INF){
            cout << -1 << "\n";
            return 0;
        }
        ttl += cmin[i];
    }
    cout << ttl << "\n";
    return 0;
}
