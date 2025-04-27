#include <iostream>
#include <vector>
#include <algorithm>
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

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;

        vl a(n);
        forn(i, 0, n) cin >> a[i];
        sort(all(a));

        vector<pair<ll, int>> cnt;
        for(ll x : a){
            if(cnt.empty() || cnt.back().f != x){
                cnt.pb({x, 1});
            } else{
                cnt.back().s++;
            }
        }

        bool flg = false;
        int m = cnt.size(), i = 0;
        while(i < m && !flg){
            int j = i;
            ll last = cnt[i].f;
            vi cap;

            while(j < m && cnt[j].f <= last + 1){
                int c = cnt[j].s;
                if(c >= 4) flg = true;
                cap.pb(min(c, 4));
                last = cnt[j].f;
                j++;
            }

            if(!flg){
                int L = cap.size();

                vi z(L + 1);
                forn(u, 0, L){
                    z[u + 1] = z[u] + (cap[u] == 0);
                }

                int lb = -1;
                forn(u, 0, L){
                    if(cap[u] >= 2){
                        if(lb != -1 && (z[u] - z[lb + 1]) == 0){
                            flg = true;
                            break;
                        }
                    lb = u;
                    }
                }
            }
            i = j;
        }
        cout << (flg ? "Yes\n" : "No\n");
    }
    return 0;
}
