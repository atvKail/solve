#include <iostream>
using namespace std;

#define forn(i, l, r) for (int i = l; i < r; ++i)
#define all(a) a.begin(), a.end()
#define f first
#define s second
using ll = long long;

ll extgcd(ll a, ll b, ll &x, ll &y) {
    if(b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    ll x1, y1;
    ll g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

pair<ll,ll> crt2(ll a1, ll n1, ll a2, ll n2) {
    ll x, y;
    ll g = extgcd(n1, n2, x, y);
    ll d = a2 - a1;
    if (d % g != 0) return {0, -1};
    ll m2 = n2 / g;
    ll k = (d / g % m2) * (x % m2) % m2;
    if(k < 0) k += m2;
    ll l = n1 / g * n2;
    ll r = (a1 + n1 * k) % l;
    if(r < 0) r += l;
    return {r, l};
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        ll t, a1, m, a2, n;
        cin >> t >> a1 >> m >> a2 >> n;
        ll r1 = 0, mod1 = t;
        ll r2 = (m - a1 % m) % m, mod2 = m;
        ll r3 = (n - ((a1 + a2) % n)) % n, mod3 = n;

        auto p12 = crt2(r1, mod1, r2, mod2);
        if(p12.s < 0) {
            cout << -1 << "\n";
            continue;
        }

        pair<ll, ll> p123 = crt2(p12.f, p12.s, r3, mod3);
        cout << (p123.s < 0 ? -1 : p123.f) << "\n";
    }
    return 0;
}
