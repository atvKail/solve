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

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        ll w, h, a, b;
        cin >> w >> h >> a >> b;
        ll x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;

        ll rx1 = ((x1 % a) + a) % a;
        ll rx2 = ((x2 % a) + a) % a;
        ll ry1 = ((y1 % b) + b) % b;
        ll ry2 = ((y2 % b) + b) % b;

        bool rowwise = false, colwise = false;
        if (ry1 == ry2) {
            if ( llabs(y1 - y2) >= b || rx1 == rx2 )
                rowwise = true;
        }

        if (rx1 == rx2) {
            if ( llabs(x1 - x2) >= a || ry1 == ry2 )
                colwise = true;
        }

        cout << ((rowwise || colwise) ? "Yes\n" : "No\n");
    }
    return 0;
}

// SOLVED