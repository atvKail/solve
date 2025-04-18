#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define forn(i, a, b) for (int i = a; i < b; i++)
using ll = long long;
const ll MOD = 998244353;

ll modExp(ll base, ll exp) {
    ll res = 1;
    while(exp > 0) {
        if(exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> graph(n + 1);
        forn (i, 0, m) {
            int u, v;
            cin >> u >> v;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        ll res = 1;
        vector<int> clr(n + 1, -1);
        forn (i, 1, n + 1) {
            if(clr[i] == -1) {
                int cnt0 = 0, cnt1 = 0;
                bool bip = true;
                queue<int> q;
                clr[i] = 0;
                q.push(i);
                while(!q.empty() && bip){
                    int cur = q.front();
                    q.pop();
                    if(clr[cur] == 0) cnt0++;
                    else cnt1++;
                    for(auto nxt : graph[cur]) {
                        if (clr[nxt] == -1) {
                            clr[nxt] = clr[cur] ^ 1;
                            q.push(nxt);
                        } else if (clr[nxt] == clr[cur]) {
                            bip = false;
                            break;
                        }
                    }
                }
                if (!bip) {
                    res = 0;
                    break;
                }
                ll ways = (modExp(2, cnt0) + modExp(2, cnt1)) % MOD;
                res = (res * ways) % MOD;
            }
        }
        cout << res % MOD << "\n";
    }
    return 0;
}
