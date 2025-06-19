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
using vvll = vector<vll>;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--){
        int n, m, k;
        cin >> n >> m >> k;
        vector<string> grid(n);
        forn(i, 0, n){
            cin >> grid[i];
        }
        ll ttlg = 0;
        forn(i, 0, n){
            forn(j, 0, m){
                if(grid[i][j] == 'g') ttlg++;
            }
        }
        vvll ps(n + 1, vll(m + 1, 0));
        forn(i, 0, n){
            forn(j, 0, m){
                ps[i + 1][j + 1] = ps[i][j + 1] + ps[i + 1][j] - ps[i][j] + (grid[i][j] == 'g');
            }
        }
        ll blost = LLONG_MAX;
        
        if(k == 0){
            blost = 0;
        } else{
            int d = k - 1; 
            forn(i, 0, n){
                forn(j, 0, m){
                    if(grid[i][j] != '.') continue;
                    int r1 = max(0, i - d);
                    int c1 = max(0, j - d);
                    int r2 = min(n - 1, i + d);
                    int c2 = min(m - 1, j + d);
                    if(r1 > r2 || c1 > c2){
                        
                        blost = 0;
                    } else{
                        ll lost = ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1];
                        blost = min(blost, lost);
                    }
                }
            }
        }
        ll res = ttlg - blost;
        cout << res << '\n';
    }
    return 0;
}

// SOLVED