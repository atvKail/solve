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
    int t;
    cin >> t;
    while(t--){
        int x, y, a;
        cin >> x >> y >> a;

        int r = a % (x + y);
        if(r < x){
            cout << "NO\n";
        } else{
            cout << "YES\n";
        }
    }
}
