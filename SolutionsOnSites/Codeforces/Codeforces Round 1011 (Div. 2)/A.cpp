#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

#define forn(l, n) for(int i = l; i < n; i++)
using ll = long long;
using ld = long int;
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;
        string s;
        cin >> s;

        bool allSame = true;
        forn (1, n){
            if(s[i] != s[0]){
                allSame = false;
                break;
            }
        }
        if(allSame){
            cout << "NO" << endl;
            continue;
        }
 
        string rev = s;
        reverse(rev.begin(), rev.end());
        if(s < rev){
            cout << "YES" << endl;
        } else {
            if(k >= 1)
                cout << "YES" << endl;
            else
                cout << "NO" << endl;
        }
    }
    return 0;
}

// Solved