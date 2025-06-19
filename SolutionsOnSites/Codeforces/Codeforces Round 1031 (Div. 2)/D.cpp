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
using vll = vector<ll>;
using vvi = vector<vi>;
using vvll = vector<vll>;

int cntwins(const vi &a, const vi &b){
    int n = a.size();
    int i = 0, j = 0, wins = 0;
    forn(k, 0, n){
        if(a[i] > b[j]){
            wins++;
            i++;
        } else{
            j++;
        }
    }
    return wins;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vi a(n), b(n);
        forn(i, 0, n) cin >> a[i];
        forn(i, 0, n) cin >> b[i];

        vi pref_min(n);
        pref_min[0] = 0;
        forn(i, 1, n){
            pref_min[i] = pref_min[i-1];
            if(a[i] < a[pref_min[i-1]])
                pref_min[i] = i;
        }
        vi suf_max(n);
        suf_max[n-1] = n-1;
        for(int i = n-2; i >= 0; --i){
            suf_max[i] = suf_max[i+1];
            if(a[i] > a[suf_max[i+1]])
                suf_max[i] = i;
        }

        int cur = cntwins(a, b);
        int lo = cur, hi = n;
        while(hi - lo > 1){
            int mid = lo + (hi - lo) / 2;
            int lpos = pref_min[mid-1];
            int rpos = suf_max[mid];
            swap(a[lpos], a[rpos]);
            int cw = cntwins(a, b);
            swap(a[lpos], a[rpos]);
            if(cw >= mid) lo = mid;
            else hi = mid;
        }
        cout << lo << '\n';
    }
    return 0;
}

// SOLVED