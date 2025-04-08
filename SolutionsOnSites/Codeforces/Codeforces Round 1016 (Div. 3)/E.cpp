#include <iostream>
#include <vector>
using namespace std;

#define forn(l, n) for (int i = l; i < n; i++)
#define all(a) a.begin(), a.end()
using ll = long long;
using ld = long int;

bool canSegment(const vector<int>& a, int n, int k, int x) {
    if(x == 0) return true;
    int cnt = 0, dct = 0;
    vector<bool> found(x, false);
    for (int i = 0; i < n; i++) {
        int val = a[i];
        if(val < x && !found[val]) {
            found[val] = true;
            dct++;
        }
        if(dct == x) {
            cnt++;
            dct = 0;
            for (int j = 0; j < x; j++)
                found[j] = false;
        }
    }
    return cnt >= k;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;
        
        vector<int> a(n);
        forn(0, n) {
            cin >> a[i];
        }

        int l = 0, r = n + 1;
        while(l < r) {
            int m = (l + r + 1) / 2;
            if(canSegment(a, n, k, m))
                l = m;
            else
                r = m - 1;
        }
        cout << l << "\n";
    }
    return 0;
}
