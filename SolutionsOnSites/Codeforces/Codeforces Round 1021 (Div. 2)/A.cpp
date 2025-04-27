#include <iostream>
#include <vector>
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
    const int TH[10] ={9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
    while(t--){
        string s;
        cin >> s;

        vi cnt(10);
        forn(i, 0, 10) cnt[s[i] - '0']++;
        string res;
        res.reserve(10);
        
        forn(i, 0, 10){
            for(int d = TH[i]; d <= 9; ++d){
                if(cnt[d]){
                    res.pb('0' + d);
                    cnt[d]--;
                    break;
                }
            }
        }
        cout << res << "\n";
    }
    return 0;
}
