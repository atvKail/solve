#include <iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <queue>
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
using vvi = vector<vi>;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        int n;
        cin >> n;
        int m = n - 2;
        vector<array<int, 3>> tri(m);
        forn(i, 0, m) cin >> tri[i][0] >> tri[i][1] >> tri[i][2];

        vector<pair<pii, int>> edgs;
        edgs.reserve(3 * m);
        forn(i, 0, m){
            auto &t = tri[i];
            forn(e, 0, 3){
                int u = t[e], v = t[(e + 1) % 3];
                if(u > v) swap(u, v);
                edgs.pb(mp(mp(u, v), i));
            }
        }

        sort(all(edgs), [](auto &A, auto &B){
            if(A.f != B.f) return A.f < B.f;
            return A.s < B.s;
        });

        vvi dladj(m);
        vvi bdradj(n + 1);
        int sz = edgs.size();
        for(int i = 0; i < sz;){
            int j = i + 1;
            while(j < sz && edgs[j].f == edgs[i].f) ++j;
            if(j - i == 1){
                int u = edgs[i].f.f;
                int v = edgs[i].f.s;
                bdradj[u].pb(v);
                bdradj[v].pb(u);
            } else{
                int t1 = edgs[i].s;
                int t2 = edgs[i + 1].s;
                dladj[t1].pb(t2);
                dladj[t2].pb(t1);
            }
            i = j;
        }

        vi p;
        p.reserve(n);
        int start = 1;
        while(bdradj[start].size() != 2) ++start;
        p.pb(start);
        int prev = -1, cur = start;
        forn(step, 1, n){
            auto &nbr = bdradj[cur];
            int nxt = (nbr[0] == prev ? nbr[1] : nbr[0]);
            p.pb(nxt);
            prev = cur;
            cur = nxt;
        }

        vi deg(m), q;
        q.reserve(m);
        queue<int> Q;
        forn(i, 0, m){
            deg[i] = dladj[i].size();
            if(deg[i] <= 1) Q.push(i);
        }
        while(!Q.empty()){
            int t = Q.front(); Q.pop();
            q.pb(t);
            for(int to: dladj[t]){
                if(--deg[to] == 1) Q.push(to);
            }
        }

        for(int x: p) cout << x << ' ';
        cout << '\n';
        forn(i, 0, m){
            cout << q[i] + 1 << (i + 1<m? ' ' : '\n');
        }
    }
    return 0;
}
