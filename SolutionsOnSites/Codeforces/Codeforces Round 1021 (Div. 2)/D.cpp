#pragma GCC optimize("O3,unroll-loops")

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
using vl = vector<ll>;
using vvi = vector<vi>;
using vvl = vector<vl>;

const int MOD = 1e9 + 7;

int dx[4] ={-1, 0, 1, 0};
int dy[4] ={0, 1, 0, -1};

bool isValid(int x, int y, int n, int m){
    return x >= 1 && x <= n && y >= 1 && y <= m;
}

uint64_t hash_used(const vi& used, int i){
    uint64_t h = 0;
    for(int j = 0; j < i; ++j){
        if(used[j] != -1){
            h = (h * 31 + used[j]) % (1LL << 32);
        }
    }
    return h;
}

int main(){
    int t;
    cin >> t;
    while(t--){
        int n, m, k;
        cin >> n >> m >> k;

        vector<pii> p(2 * k + 1);
        forn(i, 0, k + 1){
            int x, y;
            cin >> x >> y;
            p[2 * i] = mp(x, y);
        }
        set<pii> A(all(p));

        vvi T(k);
        vector<pii> all_candidates;
        map<pii, int> candidate_index;
        forn(i, 0, k){
            int x1 = p[2 * i].f, y1 = p[2 * i].s;
            int x2 = p[2 * i + 2].f, y2 = p[2 * i + 2].s;
            forn(d, 0, 4){
                int nx = x1 + dx[d], ny = y1 + dy[d];
                if(isValid(nx, ny, n, m) && !A.count(mp(nx, ny))){
                    forn(dd, 0, 4){
                        int nnx = nx + dx[dd], nny = ny + dy[dd];
                        if(isValid(nnx, nny, n, m) && nnx == x2 && nny == y2){
                            if(!candidate_index.count(mp(nx, ny))){
                                candidate_index[mp(nx, ny)] = all_candidates.size();
                                all_candidates.pb(mp(nx, ny));
                            }
                            T[i].pb(candidate_index[mp(nx, ny)]);
                            break;
                        }
                    }
                }
            }
        }

        unordered_map<uint64_t, int> memo;
        function<int(int, vi&)> dp = [&](int i, vi& used) -> int{
            if(i == k) return 1;
            uint64_t key = (static_cast<uint64_t>(i) << 32) | hash_used(used, i);
            if(memo.count(key)) return memo[key];

            int res = 0;
            for(int c : T[i]){
                bool valid = true;
                for(int j = 0; j < i; ++j){
                    if(used[j] == c){
                        valid = false;
                        break;
                    }
                }
                if(valid){
                    used[i] = c;
                    res = (res + dp(i + 1, used)) % MOD;
                    used[i] = -1;
                }
            }
            return memo[key] = res;
        };

        vi initial_used(k, -1);
        cout << dp(0, initial_used) << "\n";
    }
    return 0;
}
// TL 7