#include <iostream>
#include <cstdlib>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while(t--){
        int n, k, p;
        cin >> n >> k >> p;
        if(k == 0){
            cout << 0 << "\n";
            continue;
        }
        int absK = abs(k);
        int m = (absK + p - 1) / p;
        if(m > n)
            cout << -1 << "\n";
        else
            cout << m << "\n";
    }
    return 0;
}
