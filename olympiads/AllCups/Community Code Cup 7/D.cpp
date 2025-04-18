#include <iostream>
#include <vector>
using namespace std;

#define forn(i, l, r) for (int i = l; i < r; ++i)
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<int> p(n * m);
    forn(i, 0, n) forn(j, 0, m) cin >> p[i * m + j];

    vector<int> hlen(n * m);
    ll res = 0;

    forn(i, 0, n) {
        for(int j = m - 1; j >= 0; --j) {
            int idx = i * m + j;
            if(j + 1 < m && p[idx + 1] == p[idx] + 1) {
                hlen[idx] = hlen[idx + 1] + 1;
            } else {
                hlen[idx] = 1;
            }
            res += hlen[idx];
        }
    }

    if(n > 1) {
        vector<int> diff(n - 1);
        forn(j, 0, m) {
            forn(i, 0, n - 1) {
                diff[i] = p[(i + 1) * m + j] - p[i * m + j];
            }
            int i = 0;
            while(i < n - 1) {
                int v = diff[i], start = i;
                while(i < n - 1 && diff[i] == v) i++;
                int end = i - 1;
                if(v > 0) {
                    int cnt = 0;
                    forn(row, start, end + 2) {
                        if(hlen[row * m + j] >= v) cnt++;
                        else if(cnt >= 2) {
                            res += (ll)cnt * (cnt - 1) / 2;
                            cnt = 0;
                        } else
                            cnt = 0;
                    }
                    if(cnt >= 2) {
                        res += (ll)cnt * (cnt - 1) / 2;
                    }
                }
            }
        }
    }
    cout << res << "\n";
    return 0;
}
