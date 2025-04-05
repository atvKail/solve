#include <iostream>
#include <vector>
using namespace std;

#define forn(l, n) for(int i = l; i < n; i++)
using ll = long long;
using ld = long int;

int gcd(int a,int b){
    if(b == 0)
        return a;
    else
        return (b == 0) ? a : gcd(b,a%b);  
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<ll> a(n);
        forn(0, n){
            cin >> a[i];
        }

        ll m = a[0];
        forn(1, n){
            if(a[i] < m) m = a[i];
        }

        int count_m = 0;
        vector<ll> d;
        forn(0, n){
            if(a[i] % m == 0) d.push_back(a[i]);
            if(a[i] == m) count_m++;
        }

        if(count_m >= 2){
            cout << "Yes\n";
            continue;
        }

        if((int)d.size() <= 1){
            cout << "No\n";
            continue;
        }

        bool removed = false;
        ll g = 0;
        for(ll x : d){
            if(x == m && !removed){
                removed = true;
                continue;
            }
            ll div = x / m;
            g = (g == 0 ? div : gcd(g, div));
        }

        cout << (g == 1 ? "Yes\n" : "No\n");
    }
    return 0;
}
