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
        int n, k;
        cin >> n >> k;

        vi a(n);
        forn(i, 0, n){
            cin >> a[i];
        }

        sort(all(a));
        
        vll freq;
        freq.reserve(n);
        for(int i = 0, j; i < n; i = j){
            j = i + 1;
            while(j < n && a[j] == a[i]) j++;
            freq.pb(j - i);
        }

        int m = freq.size(); 
        sort(all(freq));

        ll sum = 0;
        int trem = 0;
        for(ll f : freq){
            if(sum + f <= k){
                sum += f;
                trem++;
            } else{
                break;
            }
        }
        int res = m - trem;
        res = max(res, 1);
        cout << res << "\n";
    }
    return 0;
}
