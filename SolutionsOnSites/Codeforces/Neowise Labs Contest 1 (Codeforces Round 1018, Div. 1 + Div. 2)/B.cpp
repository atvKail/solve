#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define forn(i, l, r) for(int i = l; i < r; ++i)
#define all(a) a.begin(), a.end()
#define f first
#define s second
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;
        vector<ll> l(n), r(n), m(n);

        ll S = 0;
        forn(i, 0, n){
            cin >> l[i];
        }
        forn(i, 0, n){
            cin >> r[i];
        }
        forn(i, 0, n){
            ll mi = min(l[i], r[i]);
            ll Mi = max(l[i], r[i]);
            S += Mi;
            m[i] = mi;
        }
        sort(all(m), greater<ll>());

        ll add = 0;
        forn(i, 0, k - 1) add += m[i];

        cout << S + add + 1 << "\n";
    }
    return 0;
}
