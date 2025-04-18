#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define forn(i, a, b) for (int i = a; i < b; i++)
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    vector<int> w(n);
    int max_d = 0;
    forn(i, 0, n){
        cin >> w[i];
        max_d = max(max_d, w[i]);
    }
    vector<ll> freq(max_d + 51, 0);
    forn(i, 0, n) freq[w[i]]++;
    
    ll carry = 0;
    int res = 0;
    forn(d, 0, max_d + 51){
        ll ttl = freq[d] + carry;
        if(ttl % 2 == 1) res++;
        carry = ttl / 2;
    }
    
    cout << res << "\n";
    return 0;
}
