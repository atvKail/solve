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
using vb = vector<bool>;
using vvi = vector<vi>;
using vll = vector<ll>;
using unomapss = unordered_map<string, string>;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    int t;
    cin >> t;
    while (t--) {
        int n, x;
        cin >> n >> x;
        
        vll a(n);
        forn(i, 0, n) {
            cin >> a[i];
        }

        if(x <= n / 2) {
            cout << "YES\n";
            continue;
        }

        vll b = a;
        sort(all(b));

        int l = n - x;    
        int r = x - 1;    

        bool flg = true;
        forn(i, l, r + 1) {
            if(a[i] != b[i]) {
                flg = false;
                break;
            }
        }
        cout << (flg ? "YES\n" : "NO\n");
    }
    return 0;
}
