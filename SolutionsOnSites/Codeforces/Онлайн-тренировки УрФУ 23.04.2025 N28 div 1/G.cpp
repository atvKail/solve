#include <iostream>
#include <vector>
using namespace std;

#define forn(i, l, r) for(int i = l; i < r; ++i)
#define all(a) (a).begin(), (a).end()
#define f first
#define s second
#define pb push_back

using ll = long long;
using vi = vector<int>;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--){
        int n;
        cin >> n;
        string s;
        cin >> s;

        vi pos;
        pos.reserve(n);
        forn(i, 0, n){
            if (s[i] == '*') pos.pb(i);
        }

        int m = pos.size();
        if (m <= 1){
            cout << 0 << '\n';
            continue;
        }
        forn(i, 0, m){
            pos[i] = pos[i] - i;
        }

        int med = pos[m / 2];
        ll res = 0;
        forn(i, 0, m){
            res += (ll)(abs(pos[i] - med));
        }
        cout << res << '\n';
    }
    return 0;
}
