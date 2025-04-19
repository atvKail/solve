#include <iostream>
using namespace std;

#define forn(i, l, r) for(int i = l; i < r; ++i)
#define all(a) a.begin(), a.end()
#define f first
#define s second
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; 
    cin >> T;
    while(T--){
        int n;
        cin >> n;

        ll sx = 0, su = 0;
        forn(i, 0, n){
            ll x, y;
            cin >> x >> y;
            sx ^= x;
            su ^= (x + y);
        }

        ll s = sx;
        ll t = su - sx;
        cout << s << " " << t << "\n";
    }
    return 0;
}
