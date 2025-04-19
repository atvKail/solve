#include <iostream>
#include<vector>
using namespace std;

#define forn(i, l, r) for (int i = l; i < r; ++i)
#define all(a) a.begin(), a.end()
#define f first
#define s second
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n;
        string s;
        cin >> n >> s;

        int cnt = 0;
        for(char c : s) {
            if(c == '<') cnt++;
        }

        vector<int> a(n);
        a[0] = cnt + 1;

        vector<int> lo, hi;
        lo.reserve(cnt);
        hi.reserve(n - cnt - 1);

        forn(x, 1, cnt + 1){
            lo.push_back(x);
        }
        forn(x, cnt + 2, n + 1){
            hi.push_back(x);
        }
        int hip = 0;
        forn(i, 0, n - 1){
            if(s[i] == '<'){
                a[i + 1] = lo.back();
                lo.pop_back();
            } else {
                a[i+1] = hi[hip++];
            }
        }
        for(int v : a) cout << v << " ";
        cout << "\n";
    }
    return 0;
}
