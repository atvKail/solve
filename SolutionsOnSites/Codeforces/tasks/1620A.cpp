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

struct DSU{
    vi p;
    DSU(int n): p(n){
        iota(all(p), 0);
    }
    int find(int x){
        return p[x] == x ? x : p[x] = find(p[x]);
    }
    void unite(int a, int b){
        a = find(a);
        b = find(b);
        if(a != b) p[b] = a;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--){
        string s;
        cin >> s;
        int n = s.size();
        DSU dsu(n);

        forn(i, 0, n){
            if(s[i] == 'E'){
                int j = (i + 1) % n;
                dsu.unite(i, j);
            }
        }
        
        bool flg = true;
        forn(i, 0, n){
            if (s[i] == 'N'){
                int j = (i + 1) % n;
                if(dsu.find(i) == dsu.find(j)){
                    flg = false;
                    break;
                }
            }
        }
        cout << (flg ? "YES\n" : "NO\n");
    }
    return 0;
}
