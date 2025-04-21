#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define forn(i, l, r) for (int i = l; i < r; ++i)
#define all(a) a.begin(), a.end()
#define f first
#define s second
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        vector<int> a(n);
        forn(i, 0, n) {
            cin >> a[i];
        }

        sort(all(a));
        int res = unique(all(a)) - a.begin();
        cout << res << "\n";
    }
    return 0;
}
