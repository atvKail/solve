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
using vb = vector<bool>;
using vvi = vector<vi>;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vi p(n + 1), inv(n + 1);
        forn(i, 1, n + 1){
            cin >> p[i];
        }
        string s;
        cin >> s;
        s = " " + s;

        forn(i, 1, n + 1){
            inv[p[i]] = i;
        }
        vi clr(n + 1);
        forn(v, 1, n + 1){
            clr[v] = (s[inv[v]] == '0' ? 1 : 0);
        }
        vb used(n + 1, false);
        vi F(n + 1, 0);

        forn(i, 1, n + 1){
            if(!used[i]){
                vi cycle;
                int v = i;
                while(!used[v]){
                    used[v] = true;
                    cycle.push_back(v);
                    v = p[v];
                }
                int cnt = 0;
                for(int x : cycle){
                    cnt += clr[x];
                }
                for(int x : cycle){
                    F[x] = cnt;
                }
            }
        }
        forn(i, 1, n + 1){
            cout << F[i] << (i < n ? ' ' : '\n');
        }
    }
    return 0;
}
