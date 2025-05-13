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
    while(t--){
        ll n;
        int k;
        cin >> n >> k;

        vll d(k);
        forn(i, 0, k){
            ll x;
            cin >> x;
            d[i] = n - x;
        }

        sort(all(d));
        ll sum = 0;
        int ans = 0;
        for(ll di : d){
            if(sum + di < n){
                sum += di;
                ans++;
            } else{
                break;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}
