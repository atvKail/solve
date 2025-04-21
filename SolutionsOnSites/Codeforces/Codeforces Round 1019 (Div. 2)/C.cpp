#include <iostream>
#include <vector>
#include <climits>
using namespace std;

#define forn(i, l, r) for (int i = l; i < r; ++i)
#define all(a) a.begin(), a.end()
#define f first
#define s second
using ll = long long;

bool solve_one(const vector<int>& a){
    int n = (int) a.size() - 1;
    if (n < 3){
        return false;
    }
    vector<bool> p(n + 2, false), s(n + 2, false);
    int c = 0;
    forn(i, 1, n + 1){
        c += a[i];
        if (2 * c >= i + (i & 1)){
            p[i] = true;
        }
    }
    c = 0;
    for (int i = n; i >= 1; --i){
        c += a[i];
        int L = n - i + 1;
        if (2 * c >= L + (L & 1)){
            s[i] = true;
        }
    }
    vector<bool> sa(n + 3, false);
    for (int i = n; i >= 1; --i){
        sa[i] = s[i] || sa[i + 1];
    }
    forn(l, 1, n - 1){
        if (p[l] && sa[l + 2]){
            return true;
        }
    }
    vector<ll> C(n + 1, 0);
    forn(i, 1, n + 1){
        C[i] = C[i - 1] + (a[i] ? 1 : -1);
    }
    ll NEG = LLONG_MIN / 4;
    vector<ll> m0(n + 2, NEG), m1(n + 2, NEG);
    m0[n] = m1[n] = NEG;
    for (int i = n - 1; i >= 1; --i){
        m0[i] = m0[i + 1];
        m1[i] = m1[i + 1];
        if ((i & 1) == 0){
            m0[i] = max(m0[i], C[i]);
        } else{
            m1[i] = max(m1[i], C[i]);
        }
    }
    forn(l, 1, n - 1){
        if (!p[l]){
            continue;
        }
        int st = l + 1;
        if (st > n - 1){
            break;
        }
        ll B = C[st - 1];
        int lp = l & 1;
        if (m0[st] != NEG && lp == 0 && m0[st] >= B){
            return true;
        }
        if (m1[st] != NEG && lp == 1 && m1[st] >= B){
            return true;
        }
        if (m0[st] != NEG && lp == 1 && m0[st] >= B + 1){
            return true;
        }
        if (m1[st] != NEG && lp == 0 && m1[st] >= B + 1){
            return true;
        }
    }
    return false;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--){
        int n;
        ll k;
        cin >> n >> k;

        vector<int> a(n + 1);
        forn(i, 1, n + 1){
            ll x;
            cin >> x;
            a[i] = (x <= k);
        }

        bool f = solve_one(a);
        if (!f){
            vector<int> rb(n + 1);
            forn(i, 1, n + 1){
                rb[i] = a[n - i + 1];
            }
            f = solve_one(rb);
        }
        cout << (f ? "YES\n" : "NO\n");
    }
    return 0;
}
