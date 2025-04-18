#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define forn(i, a, b) for (int i = a; i < b; i++)
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<int> a(n);
        forn(i, 0, n) {
            cin >> a[i];
        }
        int lb = 0, ub = 1000000000;
        forn(i, 0, n-1){
            if(a[i] < a[i + 1]){
                int curU = (a[i] + a[i + 1]) / 2;
                ub = min(ub, curU);
            }
            else if(a[i] > a[i+1]){
                int curL = (a[i] + a[i + 1] + 1) / 2;
                lb = max(lb, curL);
            }
        }
        cout << (lb <= ub ? lb : -1) << "\n";
    }
    return 0;
}
