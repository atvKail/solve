#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define forn(i, l, r) for(int i = l; i < r; ++i)
#define all(a) (a).begin(), (a).end()
#define f first
#define s second

using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll n;
    int m;
    cin >> n >> m;

    vector<ll> d(m);
    forn(i, 0, m) cin >> d[i];
    sort(all(d));

    if ((m > 0 && d.front() == 1) || (m > 0 && d.back() == n)) {
        cout << "NO\n";
        return 0;
    }

    forn(i, 0, m - 2) {
        if (d[i + 2] - d[i] == 2) {
            cout << "NO\n";
            return 0;
        }
    }

    cout << "YES\n";
    return 0;
}
