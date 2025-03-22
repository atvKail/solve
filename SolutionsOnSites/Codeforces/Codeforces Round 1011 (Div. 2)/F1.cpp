#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

#define forn(l, n) for(int i = l; i < n; i++)
using ll = long long;
using ld = long int;
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;
        
        vector<int> a(n + 1);
        forn (1, n + 1){
            cin >> a[i];
        }
        vector<vector<int>> pos(k + 1);
        forn (1, n + 1){
            pos[a[i]].push_back(i);
        }

        const int INF = 1e9;
        vector<int> sumDist(n+1, 0);
 
        forn (1, k + 1){
            const vector<int>& occ = pos[i];
            int p = 0;
            for (int j = 1; j <= n; j++){
                while(p + 1 < (int)occ.size() && abs(occ[p + 1]-j) <= abs(occ[p] - j)){
                    p++;
                }
                int d = abs(occ[p] - j);
                sumDist[j] += d;
            }
        }
 
        int best = INF;
        for (int j = 1; j <= n; j++){
            best = min(best, sumDist[j]);
        }
 
        int m = (k+1) / 2;
        int constCost = 0;
        for (int i = 1; i <= k; i++){
            constCost += abs(i - m);
        }
 
        int ans = best - constCost;
        cout << ans << "\n";
    }
    return 0;
}

// Solved