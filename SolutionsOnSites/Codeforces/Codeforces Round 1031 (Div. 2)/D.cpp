#include <bits/stdc++.h>
using namespace std;

#define forn(i, l, r) for (int i = l; i < r; ++i)
#define all(a) (a).begin(), (a).end()
#define f first
#define s second
#define pb push_back
#define mp make_pair

using ll = long long;
using pii = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vi>;

int simulate(const vi& a, const vi& b, int n){
    deque<int> pa(all(a)), pb(all(b));
    int score = 0;
    forn(i, 0, n){
        int x = pa.front(), y = pb.front();
        pa.pop_front(); 
        pb.pop_front();
        if(x > y){
            score++;
            pb.push_front(y);
        } else{
            pa.push_front(x);
        }
    }
    return score;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; 
    cin >> t;
    while (t--){
        int n;
        cin >> n;
        vi a(n), b(n);
        forn(i, 0, n) cin >> a[i];
        forn(i, 0, n) cin >> b[i];

        int max_score = simulate(a, b, n);

        forn(i, 0, n) forn(j, i + 1, n){
            vi a_sw = a;
            swap(a_sw[i], a_sw[j]);
            max_score = max(max_score, simulate(a_sw, b, n));
        }

        cout << max_score << "\n";
    }
    return 0;
}

// TL 4