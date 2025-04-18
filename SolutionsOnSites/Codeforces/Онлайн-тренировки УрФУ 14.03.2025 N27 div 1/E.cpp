#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define forn(i, a, b) for (int i = a; i < b; i++)
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> grdn(n, vector<int>(m));
    forn(i, 0, n) {
        forn(j, 0, m) {
            cin >> grdn[i][j];
        }
    }

    int a, b;
    cin >> a >> b;

    vector<vector<int>> pref(n + 1, vector<int>(m + 1, 0));
    forn(i, 1, n + 1) {
        forn(j, 1, m + 1) {
            int t = grdn[i - 1][j - 1] + pref[i - 1][j];
            t += pref[i][j - 1] - pref[i - 1][j - 1];
            pref[i][j] = t;
        }
    }

    auto getSum = [&](int r, int c, int h, int w) -> int {
        int r2 = r + h - 1, c2 = c + w - 1;
        return pref[r2][c2] - pref[r - 1][c2] - pref[r2][c - 1] + pref[r - 1][c - 1];
    };

    int res = 1e9;
    auto tryRectangle = [&](int h, int w) {
        if (h > n || w > m) return;
        forn(i, 1, n - h + 2) {
            forn(j, 1, m - w + 2) {
                res = min(res, getSum(i, j, h, w));
            }
        }
    };

    tryRectangle(a, b);
    tryRectangle(b, a);

    cout << res << "\n";   
}
