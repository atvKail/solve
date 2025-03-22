#include <iostream>
using namespace std;

#define forn(l, n) for(int i = l; i < n; i++)
using ull = unsigned long long;
using ll = long long;
using ld = long int;

const ull INF = 1e19;
const int L = 61;

ull memo[L+1][2][2];
bool seen[L+1][2][2];

ull dp(int i, int cx, int cy, ull x, ull y) {
    if(i == L) {
        return (cx == 0 && cy == 0) ? 0 : INF;
    }
    if(seen[i][cx][cy]) {
        return memo[i][cx][cy];
    }
    
    ull best = INF;
    int ax = (x >> i) & 1;
    int ay = (y >> i) & 1;
    
    for(int r = 0; r < 2; r++){
        int sumx = ax + r + cx;
        int sumy = ay + r + cy;
        int rx = sumx & 1;
        int ry = sumy & 1;
        if(rx && ry) {
            continue;
        }

        int ncx = sumx >> 1;
        int ncy = sumy >> 1;
        ull sub = dp(i + 1, ncx, ncy, x, y);
        if(sub == INF) {
            continue;
        }

        ull cand = ((ull)r << i) + sub;
        best = min(best, cand);
    }
    
    seen[i][cx][cy] = true;
    memo[i][cx][cy] = best;
    return best;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while (t--){
        ull x, y;
        cin >> x >> y;
        if(x == y) {
            cout << -1 << endl;
            continue;
        }
        forn(0, L + 1) {
            for(int j = 0; j < 2; j++) {
                for (int k = 0; k < 2; k++) {
                    seen[i][j][k] = false;
                }
            }
        }
        
        ull ans = dp(0, 0, 0, x, y);
        if(ans >= INF)
            cout << -1 << endl;
        else
            cout << ans << endl;
    }
    return 0;
}

// Solved