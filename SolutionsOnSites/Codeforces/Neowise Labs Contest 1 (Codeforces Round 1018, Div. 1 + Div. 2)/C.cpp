#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
using namespace std;

#define forn(i, l, r) for(int i = l; i < r; ++i)
#define all(a) a.begin(), a.end()
#define f first
#define s second
using ll = long long;
const ll INF = (ll)4e18;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;

        vector<vector<ll>> h(n, vector<ll>(n));
        forn(i, 0, n){
            forn(j, 0, n){
                cin >> h[i][j];
            }
        }

        vector<ll> a(n), b(n);
        forn(i, 0, n) cin >> a[i];
        forn(j, 0, n) cin >> b[j];

        vector<bool> f0(n - 1, false), fpos(n - 1, false), fneg(n - 1, false);
        forn(i, 0, n-1){
            forn(j, 0, n){
                ll d = h[i + 1][j] - h[i][j];
                if(d == 0) f0[i] = true;
                else if(d == 1) fpos[i] = true;
                else if(d == -1) fneg[i] = true;
            }
        }

        array <ll, 2> dp, ndp;
        dp[0] = 0; 
        dp[1] = a[0];
        forn(i, 0, n - 1){
            ndp[0] = ndp[1] = INF;
            forn(u, 0, 2){
                if(dp[u] < INF){
                    forn(v, 0, 2){
                        ll d = u - v;
                        if((d == 0 && f0[i]) || (d == 1 && fpos[i]) || (d == -1 && fneg[i]))
                            continue;
                        ndp[v] = min(ndp[v], dp[u] + (v ? a[i + 1] : 0));
                    }
                }
            }
            dp = ndp;
        }

        ll bX = min(dp[0], dp[1]);
        vector<bool> g0(n - 1, false), gpos(n - 1, false), gneg(n - 1, false);
        forn(j, 0, n - 1){
            forn(i, 0, n){
                ll d = h[i][j + 1] - h[i][j];

                if(d == 0) g0[j] = true;
                else if(d == 1) gpos[j] = true;
                else if(d == -1) gneg[j] = true;
            }
        }

        dp[0] = 0;
        dp[1] = b[0];
        forn(j, 0, n - 1){
            ndp[0] = ndp[1] = INF;
            forn(u, 0, 2){
                if(dp[u] < INF){
                    forn(v, 0, 2){
                        ll d = u - v;
                        if((d == 0 && g0[j]) || (d == 1 && gpos[j]) || (d == -1 && gneg[j]))
                            continue;
                        ndp[v] = min(ndp[v], dp[u] + (v ? b[j + 1] : 0));
                    }
                }
            }
            dp = ndp;
        }

        ll bY = min(dp[0], dp[1]);
        ll res = (bX < INF && bY < INF ? bX + bY : -1LL);
        cout << res << "\n";
    }
    return 0;
}
