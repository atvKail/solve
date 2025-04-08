#include <iostream>
#include <vector>
#include <string>
using namespace std;

#define forn(l, n) for (int i = l; i < n; i++)
#define all(a) a.begin(), a.end()
using ll = long long;
using ld = long int;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while(t--){
        int n, m;
        cin >> n >> m;
        vector<string> a(n);
        forn(0, n) cin >> a[i];
        
        vector<int> sfcnt(m, 0);
        vector<vector<string>> b(m, vector<string>(n));
        forn (0, m){
            for (int j = 0; j < n; j++){
                cin >> b[i][j];
                if(b[i][j] == a[j])
                    sfcnt[i]++;
            }
        }
        
        bool psble = true;
        for (int j = 0; j < n; j++){
            bool f = false;
            forn (0, m){
                if(b[i][j] == a[j]){
                    f = true;
                    break;
                }
            }
            if(!f){
                psble = false;
                break;
            }
        }
        if(!psble){
            cout << -1 << "\n";
            continue;
        }
        
        int nm = 0;
        forn (0, m){
            if(sfcnt[i] > nm)
                nm = sfcnt[i];
        }
        int res = 3 * n - 2 * nm;
        cout << res << "\n";
    }
    return 0;
}
