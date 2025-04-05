#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <numeric>
using namespace std;

#define forn(l, n) for(int i = l; i < n; i++)
using ll = long long;

struct PHash {
    size_t operator()(const pair<int,int>& p) const {
        return ((ll)p.first << 32) ^ p.second;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while(T--){
        int n; cin >> n;
        vector<int> a(n), b(n);
        forn(0,n) cin >> a[i];
        forn(0,n) cin >> b[i];

        unordered_map<pair<int,int>, vector<int>, PHash> mp;
        forn(0,n) mp[{a[i], b[i]}].push_back(i);

        vector<pair<int,int>> pr;
        int c = -1;
        bool f = true;

        for(auto &it : mp){
            int x = it.first.first, y = it.first.second;
            if(x == y) continue;
            if(x < y){
                auto jt = mp.find({y, x});
                if(jt == mp.end() || it.second.size() != jt->second.size()){
                    f = false;
                    break;
                }
                int sz = it.second.size();
                forn(0, sz) pr.push_back({ it.second[i], jt->second[i] });
            }
        }
        if(!f){
            cout << -1 << "\n";
            continue;
        }

        for(auto &it : mp){
            int x = it.first.first, y = it.first.second;
            if(x != y) continue;
            auto &v = it.second;
            int sz = v.size(), idx = 0;
            while(idx+1 < sz){
                pr.push_back({ v[idx], v[idx+1] });
                idx += 2;
            }
            if(idx < sz){
                if(c == -1) c = v[idx];
                else { f = false; break; }
            }
        }

        if(n % 2 == 1){
            if(c == -1) f = false;
        } else {
            if(c != -1) f = false;
        }
        if(!f || pr.size()*2 + (c == -1 ? 0 : 1) != n){
            cout << -1 << "\n";
            continue;
        }

        vector<int> Tperm(n, -1);
        int L = 0, R = n-1;
        for(auto &p : pr){
            if(L < R){
                int i1 = p.first, i2 = p.second;
                if(a[i1] != b[i2]) swap(i1, i2);
                Tperm[L++] = i1;
                Tperm[R--] = i2;
            }
        }
        if(n % 2 == 1) Tperm[n/2] = c;

        vector<int> cur(n), inv(n);
        iota(cur.begin(), cur.end(), 0);
        forn(0,n) inv[cur[i]] = i;

        vector<pair<int,int>> ops;
        for(int i = 0; i < n; i++){
            if(cur[i] != Tperm[i]){
                int j = inv[Tperm[i]];
                swap(cur[i], cur[j]);
                swap(inv[cur[i]], inv[cur[j]]);
                ops.push_back({i+1, j+1});
            }
        }

        cout << ops.size() << "\n";
        for(auto &op : ops) cout << op.first << " " << op.second << "\n";
    }
    return 0;
}
