#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define forn(i, a, b) for (int i = a; i < b; i++)
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n;
    vector<ll> team1(n);
    for (int i = 0; i < n; i++){
        cin >> team1[i];
    }
    cin >> m;
    vector<ll> team2(m);
    for (int i = 0; i < m; i++){
        cin >> team2[i];
    }
    
    sort(team1.begin(), team1.end());
    sort(team2.begin(), team2.end());
    
    vector<ll> cand;
    cand.push_back(0);
    for (ll d : team1) cand.push_back(d);
    for (ll d : team2) cand.push_back(d);
    sort(cand.begin(), cand.end());
    cand.erase(unique(cand.begin(), cand.end()), cand.end());
    
    int cnt1 = 0, cnt2 = 0;
    ll bdiff = -1e18, bscore1 = -1e18, fscore1 = 0, fscore2 = 0;
    
    for (ll d : cand) {
        while (cnt1 < n && team1[cnt1] <= d) cnt1++;
        while (cnt2 < m && team2[cnt2] <= d) cnt2++;
        ll score1 = 3LL * n - cnt1;
        ll score2 = 3LL * m - cnt2;
        ll diff = score1 - score2;
        if (diff > bdiff || (diff == bdiff && score1 > bscore1)) {
            bdiff = diff;
            bscore1 = score1;
            fscore1 = score1;
            fscore2 = score2;
        }
    }
    
    cout << fscore1 << ":" << fscore2 << "\n";
    return 0;
}
