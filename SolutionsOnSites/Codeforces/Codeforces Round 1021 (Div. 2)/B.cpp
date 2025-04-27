#include <iostream>
#include <vector>
#include <algorithm>
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

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;

        vi a(n);
        forn(i, 0, n) cin >> a[i];

        sort(all(a));
        vector<ll> b,cnt;
        forn(i, 0, n){
            if(i == 0 || a[i] != a[i - 1]) b.pb(a[i]), cnt.pb(1);
            else cnt.back()++;
        }

        int u = b.size();
        vector<ll> P(u), S(u + 1);
        P[0] = cnt[0];
        forn(j, 1, u){
            P[j] = P[j - 1] + cnt[j];
        }
        S[u] = 0;
        for(int j = u - 1; j >=0 ;--j){
            S[j] = S[j + 1] + cnt[j];
        }

        ll res = 0;
        auto proc=[&](ll L, ll R, ll Lc, ll Rc){
            if(L > R) return;
            ll sMinR = max(0LL,n - 2 * Lc), sMaxR = min((ll)k, 2 * Rc - n);
            ll sMinL = max(0LL,n - 2 * Rc), sMaxL = min((ll)k, 2 * Lc - n);
            if(sMinR <= sMaxR || sMinL <= sMaxL) res += R - L + 1;
        };

        if(b[0] > 1) proc(1, b[0] - 1, 0, n);
        forn(j, 0, u){
            proc(b[j], b[j], P[j], S[j]);
            if(j + 1 < u && b[j] + 1 <=b [j + 1] - 1){
                proc(b[j] + 1, b[j + 1] - 1, P[j], S[j + 1]);
            }
        }
        if(b[u - 1] < (int)1e9){
            proc(b[u - 1] + 1, (ll)1e9, n, 0);
        }
        cout << res << "\n";
    }
    return 0;
}
