#include <iostream>
#include <vector>
using namespace std;

#define forn(i, l, r) for (int i = l; i < r; ++i)
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<ll> a(n + 1), b(n + 1);
    forn(i, 1, n + 1) cin >> a[i];
    forn(i, 1, n + 1) cin >> b[i];

    ll res = 0;
    int ldiff = 0;
    forn(k, 1, n + 1){
        if(a[k] < b[k]){
            ll cntI = k - ldiff;
            ll cntJ = n - k + 1;
            res += cntI * cntJ;
        }
        if(a[k] != b[k]){
            ldiff = k;
        }
    }
    cout << res << "\n";
    return 0;
}
