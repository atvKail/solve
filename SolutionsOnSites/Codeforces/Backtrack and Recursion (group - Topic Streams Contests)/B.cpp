#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

using ll = long long;
#define all(a) a.begin(), a.end()

int n;
vector<vector<int>> childn;
vector<ll> s;
vector<vector<pair<ll, ll>>> dp;

ll solve(int v, ll x) {
    vector<pair<ll, ll>> &vec = dp[v];
    auto it = lower_bound(all(vec), x, [](const pair<ll,ll>& a, const ll &b) {
        return a.first < b;
    });
    if(it != vec.end() && it->first == x) {
        return it->second;
    }
    ll res = s[v] * x;
    if(childn[v].empty()){
        vec.insert(it, {x, res});
        return res;
    }

    int m = childn[v].size();
    ll base = x / m;
    int r = x % m;
    ll sum = 0;
    vector<ll> extras;
    extras.reserve(m);
    for (int w : childn[v]) {
        ll valb = solve(w, base);
        ll valp = solve(w, base + 1);
        sum += valb;
        extras.push_back(valp - valb);
    }
    sort(all(extras), greater<ll>());
    for (int i = 0; i < r; i++){
        sum += extras[i];
    }
    res += sum;
    vec.insert(lower_bound(all(vec), x, [](const pair<ll,ll>& a, const ll &b) {
        return a.first < b;
    }), {x, res});
    return res;
}
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int k;
        cin >> n >> k;
        childn.assign(n, vector<int>());
        s.assign(n, 0);
        dp.assign(n, vector<pair<ll,ll>>());

        for (int i = 1; i < n; i++){
            int p;
            cin >> p;
            p--;
            childn[p].push_back(i);
        }
        for (int i = 0; i < n; i++){
            cin >> s[i];
        }
        cout << solve(0, k) << "\n";
    }
    return 0;
}

// Превышено ограничение времени на тесте 4, также варианты с превышением памяти есть...