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
using vll = vector<ll>;
using vvi = vector<vi>;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--){
        int n, k, c = 0;
        cin >> n >> k;
        vi perm(n, -1);
        for(int d = k - 1; d < n; d += k){
            perm[d] = c++;
        }
        forn(i, 0, n){
            if (perm[i] == -1){
                perm[i] = c++;
            }
        }
        forn(i, 0, n){
            cout << (perm[i] + 1) << (i + 1 < n ? ' ' : '\n');
        }
    }
    return 0;
}
