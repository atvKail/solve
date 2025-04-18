#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define forn(i, a, b) for (int i = a; i < b; i++)
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    ll L;
    cin >> n >> L;
    vector<ll> c(n+1);
    forn(i, 1, n+1){
        cin >> c[i];
    }

    forn(i, 2, n+1){
        c[i] = min(c[i], 2LL * c[i-1]);
    }

    ll ttlCost = 0;
    ll res = 1LL << 62;
    ll rem = L;

    for (int i = n; i >= 1; i--) {
        ll v = 1LL << (i-1);
        ll cnt = rem / v;
        ttlCost += cnt * c[i];
        rem -= cnt * v;
        res = min(res, ttlCost + (rem > 0 ? c[i] : 0));
    }

    res = min(res, ttlCost);
    cout << res << "\n";
    return 0;
}
