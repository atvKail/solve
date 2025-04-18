#include <iostream>
#include <vector>
using namespace std;

#define forn(i, a, b) for (int i = a; i < b; i++)
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, k;
    cin >> n >> k;
    
    if(n == 1){
        if(k == 0) cout << 1 << "\n";
        else cout << -1 << "\n";
        return 0;
    }
    if(k > n - 1){
        cout << -1 << "\n";
        return 0;
    }
    
    vector<int> p(n+1);
    forn(i, 1, n+1) {
        p[i] = i;
    }
    
    int r = (n - 1) - k;
    forn(i, 2, r + 2) {
        swap(p[1], p[i]);
    }
    
    forn(i, 1, n+1) {
        cout << p[i] << " ";
    }
    cout << "\n";
    
    return 0;
}
