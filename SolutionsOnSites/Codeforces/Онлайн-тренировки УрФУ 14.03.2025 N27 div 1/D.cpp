#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

#define forn(i, a, b) for (int i = a; i < b; i++)
using ll = long long;
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int m = ceil(sqrt(n));
    vector<int> res;
    for (int i = 1; i <= n; i += m){
        int r = min(i + m - 1, n);
        for (int j = r; j >= i; j--){
            res.push_back(j);
        }
    }
    forn (i, 0, res.size()) {
        cout << res[i] << (i + 1 == res.size() ? "\n" : " ");
    }
    return 0;
}
