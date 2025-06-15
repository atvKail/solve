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
using vvi = vector<vi>;

ll calc(ll k, ll req1, ll dec1, ll req2, ll dec2) {
    ll cnt1 = 0;
    if (k >= req1) {
        cnt1 = (k - req1) / dec1 + 1;
        k -= cnt1 * dec1;
    }
    ll cnt2 = 0;
    if (k >= req2) {
        cnt2 = (k - req2) / dec2 + 1;
    }
    return cnt1 + cnt2;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        ll k, a, b, x, y;
        cin >> k >> a >> b >> x >> y;
        ll res = max(calc(k, a, x, b, y), calc(k, b, y, a, x));
        cout << res << "\n";
    }
    return 0;
}

// SOLVED