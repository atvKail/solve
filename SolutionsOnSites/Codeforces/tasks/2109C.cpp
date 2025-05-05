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
using vvi = vector<vi>;

struct DSU {
    vi p, r, cnt;
    DSU(int n): p(n + 1), r(n + 1, 0), cnt(n + 1, 0) {
        iota(all(p), 0);
    }
    int find(int x){
        return p[x] == x? x : p[x] = find(p[x]);
    }
    void unite(int a, int b){
        a = find(a);
        b = find(b);
        if(a == b) return;
        if(r[a] < r[b]) swap(a, b);
        p[b] = a;
        cnt[a] += cnt[b];
        if(r[a] == r[b]) r[a]++;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<pair<int, int>> a(n);
        forn(i, 0, n){
            cin >> a[i].f;
            a[i].s = i + 1; 
        }

        sort(all(a), greater<>());

        DSU dsu(n);
        vector<bool> pressed(n + 2, false); 
        
        ll clones = 0;

        int i = 0;
        while(i < n){
            int j = i;
            int w = a[i].f;
            
            vector<int> pos;
            while(j < n && a[j].f == w){
                pos.pb(a[j].s);
                j++;
            }
            
            sort(all(pos));
            vector<pair<int, int>> intervals;
            int L = pos[0], R = pos[0];
            forn(k, 1, pos.size()){
                if(pos[k] == R + 1){
                    R = pos[k];
                } else{
                    intervals.emplace_back(L, R);
                    L = R = pos[k];
                }
            }
            intervals.emplace_back(L, R);

            for(auto &iv : intervals){
                int l = iv.f, r = iv.s;
                
                vector<int> nghroots;
                if(l - 1 >= 1 && pressed[l - 1]){
                    nghroots.pb(dsu.find(l-1));
                }
                if(r + 1 <= n && pressed[r + 1]){
                    nghroots.pb(dsu.find(r + 1));
                }
                sort(all(nghroots));
                nghroots.erase(unique(all(nghroots)), nghroots.end());
                
                ll sumcnt = 0;
                for(int root : nghroots){
                    sumcnt += dsu.cnt[root];
                }
                bool nnew = (sumcnt == 0);
                if(nnew){
                    clones++;
                }
                
                forn(x, l, r + 1){
                    pressed[x] = true;
                }
                forn(x, l + 1, r + 1){
                    dsu.unite(x - 1, x);
                }
                
                if(l - 1 >= 1 && pressed[l - 1]){
                    dsu.unite(l - 1, l);
                }
                if(r + 1 <= n && pressed[r + 1]){
                    dsu.unite(r, r + 1);
                }
                if(nnew){
                    int root = dsu.find(l);
                    dsu.cnt[root] = 1;
                }   
            }
            i = j;
        }
        cout << clones << "\n";
    }
    return 0;
}
