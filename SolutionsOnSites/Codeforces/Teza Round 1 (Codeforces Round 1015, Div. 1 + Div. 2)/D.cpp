#include <iostream>
#include <vector>
using namespace std;

using ll = long long;

#define forn(l, n) for(int i = l; i < n; i++)
#define pb(a) push_back(a)

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while(t--){
        int n, m, k;
        cin >> n >> m >> k;

        int f = min(n - m * k, n / (m + 1));
        int g = max(0, k - f);

        vector<int> results;
        for (int b = 0; b < m + 1; b++){
            for (int x = 0; x < f; x++){
                results.pb(x);
            }
            if(b < m){
                forn(0, g){
                    results.pb(f);
                }
            }
        }

        while(results.size() < (size_t)n){
            results.pb(f);
        }

        results.resize(n);
        for(int x : results) {
            cout << x << " ";
        }
        cout << "\n";
    }
    return 0;
}
