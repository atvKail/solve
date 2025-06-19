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
using vll = vector<ll>;
using vvi = vector<vi>;
using vvll = vector<vll>;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--){
        int n;
        cin >> n;
        vi a(n), b(n);
        forn(i, 0, n) cin >> a[i];
        forn(i, 0, n) cin >> b[i];

        unordered_map<int, vector<pii>> pos;
        pos.reserve(2 * n);
        forn(i, 0, n) pos[a[i]].pb(mp(i, 0));
        forn(i, 0, n) pos[b[i]].pb(mp(i, 1));

        vector<bool> sw(n, false);
        ll ttl = 0;
        for(auto &kv : pos){
            auto &P = kv.s;
            int k = P.size();
            if(k == 0) continue;
            ttl += min(k, 2);
            if(k >= 2){
                int i0 = P[0].f, s0 = P[0].s;
                if(s0 != 0) sw[i0] = true;
                int i1 = P[1].f, s1 = P[1].s;
                if(s1 != 1) sw[i1] = true;
            }
        }

        vi fa(n), fb(n);
        forn(i, 0, n){
            if(sw[i]){
                fa[i] = b[i];
                fb[i] = a[i];
            } else{
                fa[i] = a[i];
                fb[i] = b[i];
            }
        }

        cout << ttl << '\n';
        forn(i, 0, n) cout << fa[i] << (i + 1 < n ? ' ' : '\n');
        forn(i, 0, n) cout << fb[i] << (i + 1 < n ? ' ' : '\n');
    }
    return 0;
}
