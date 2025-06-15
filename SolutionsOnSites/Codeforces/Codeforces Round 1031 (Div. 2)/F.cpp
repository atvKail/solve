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

const int MAXN = 200010;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    forn(test, 0, t) {
        int n;
        cin >> n;

        vi a(n);
        forn(i, 0, n) cin >> a[i];
        vi b(n);
        forn(i, 0, n) cin >> b[i];

        vector<int> freqA(MAXN, 0);
        vector<int> freqB(MAXN, 0);
        forn(i, 0, n) {
            freqA[a[i]]++;
            freqB[b[i]]++;
        }

        vector<char> inA(MAXN, 0);
        vector<char> inB(MAXN, 0);

        int cntA = 0, cntB = 0;
        vector<bool> swap_pos(n, false);

        forn(i, 0, n) {
            int incnswap = (!inA[a[i]]) + (!inB[b[i]]);
            int incswap = (!inA[b[i]]) + (!inB[a[i]]);

            int future_a = freqA[a[i]] - (inA[a[i]] ? 0 : 1);
            int future_b = freqB[b[i]] - (inB[b[i]] ? 0 : 1);
            int future_swap_a = freqA[b[i]] - (inA[b[i]] ? 0 : 1);
            int future_swap_b = freqB[a[i]] - (inB[a[i]] ? 0 : 1);

            if (incnswap > incswap || 
                (incnswap == incswap && future_a + future_b >= future_swap_a + future_swap_b)) {
                swap_pos[i] = false;
                if (!inA[a[i]]) {
                    cntA++;
                    inA[a[i]] = 1;
                }
                if (!inB[b[i]]) {
                    cntB++;
                    inB[b[i]] = 1;
                }
            } else {
                swap_pos[i] = true;
                if (!inA[b[i]]) {
                    cntA++;
                    inA[b[i]] = 1;
                }
                if (!inB[a[i]]) {
                    cntB++;
                    inB[a[i]] = 1;
                }
            }

            freqA[a[i]]--;
            freqB[b[i]]--;
        }

        cout << cntA + cntB << '\n';

        forn(i, 0, n) {
            cout << (swap_pos[i] ? b[i] : a[i]) << ' ';
        }
        cout << '\n';

        forn(i, 0, n) {
            cout << (swap_pos[i] ? a[i] : b[i]) << ' ';
        }
        cout << '\n';
    }
    return 0;
}

// WA