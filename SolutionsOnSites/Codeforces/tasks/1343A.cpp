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

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while(t--){
        ll n;
        cin >> n;
        forn(k, 2, 31){
            ll s = (1LL << k) - 1;
            if(n % s == 0){
                cout << (n / s) << "\n";
                break;
            }
        }
    }
    return 0;
}
