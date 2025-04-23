#include <iostream>
using namespace std;

#define forn(i, l, r) for(int i = l; i < r; ++i)
#define all(a) (a).begin(), (a).end()
#define f first
#define s second

using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        ll n, x, y;
        cin >> n >> x >> y;
        ll mn = max(1LL, x + y - n + 1);
        if (mn > n) mn = n;
        ll mx = min(n, x + y - 1);
        cout << mn << " " << mx << "\n";
    }
    return 0;
}
