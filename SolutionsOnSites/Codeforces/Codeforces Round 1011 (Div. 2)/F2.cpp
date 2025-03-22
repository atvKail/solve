// #include <iostream>
// #include <vector>
// #include <algorithm>
// using namespace std;
 
// #define forn(l, n) for(int i = l; i < n; i++)
// using ll = long long;
// using ld = long int;

// inline void update_range(vector<ll> &diffC, vector<ll> &diffConst, int L, int R, ll A, ll B) {
//     if(L > R) return;
//     diffC[L] += A;
//     diffC[R + 1] -= A;
//     diffConst[L] += B;
//     diffConst[R + 1] -= B;
// }

// int main(){
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);

//     int t;
//     cin >> t;
//     while(t--){
//         int n, k;
//         cin >> n >> k;

//         vector<int> a(n + 1);
//         forn (1, n + 1){
//             cin >> a[i];
//         }
//         vector<vector<int>> pos(k + 1);
//         forn (1, n + 1){
//             pos[a[i]].push_back(i);
//         }
 
//         vector<ll> diffC(n + 2, 0), diffConst(n + 2, 0);
//         for (int color = 1; color <= k; color++){
//             const vector<int>& occ = pos[color];
//             if(occ.empty()) {
//                 continue;
//             }
 
//             int mOcc = occ.size();

//             update_range(diffC, diffConst, 1, occ[0], -1, occ[0]);
//             update_range(diffC, diffConst, occ[mOcc - 1], n, 1, -occ[mOcc - 1]);
 
//             forn (0, mOcc - 1){
//                 int L = occ[i], R = occ[i + 1];
//                 int mid = (L + R) / 2;
//                 update_range(diffC, diffConst, L, mid, 1, -L);
//                 update_range(diffC, diffConst, mid + 1, R, -1, R);
//             }
//         }
 
//         ll best = 1e18;
//         ll curC = 0, curConst = 0;
//         for (int j = 1; j <= n; j++){
//             curC += diffC[j];
//             curConst += diffConst[j];
//             ll val = curC * j + curConst;
//             best = min(best, val);
//         }

//         int m = (k + 1) / 2;
//         int constCost = 0;
//         for (int i = 1; i <= k; i++){
//             constCost += abs(i - m);
//         }
 
//         ll ans = best - constCost;
//         cout << ans << "\n";
//     }
//     return 0;
// } // Превышение по времени на 17 тесте


#include <iostream>
#include <vector>
#include <cstdlib>
#include <algorithm>
using namespace std;

using ll = long long;

inline void update_range(vector<ll>& diffC, vector<ll>& diffConst, int L, int R, ll A, ll B) {
    if (L > R) return;
    diffC[L] += A;
    diffC[R + 1] -= A;
    diffConst[L] += B;
    diffConst[R + 1] -= B;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        
        vector<int> a(n + 1);
        for (int i = 1; i <= n; i++) {
            cin >> a[i];
        }

        vector<vector<int>> pos(k + 1);
        for (int i = 1; i <= n; i++) {
            pos[a[i]].push_back(i);
        }
 
        vector<ll> diffC(n + 2, 0), diffConst(n + 2, 0);
        for (int color = 1; color <= k; color++) {
            const vector<int>& occ = pos[color];
            if (occ.empty()) continue;

            int mOcc = occ.size();

            update_range(diffC, diffConst, 1, occ[0], -1, occ[0]);
            update_range(diffC, diffConst, occ[mOcc - 1], n, 1, -occ[mOcc - 1]);

            for (int i = 0; i < mOcc - 1; i++) {
                int L = occ[i], R = occ[i + 1];
                int mid = (L + R) / 2;
                update_range(diffC, diffConst, L, mid, 1, -L);
                update_range(diffC, diffConst, mid + 1, R, -1, R);
            }
        }

        ll best = 1e18;
        ll curC = 0, curConst = 0;
        for (int i = 1; i <= n; i++) {
            curC += diffC[i];
            curConst += diffConst[i];
            ll val = curC * i + curConst;
            best = min(best, val);
        }

        int m = (k + 1) / 2;
        ll constCost = 0;
        for (int i = 1; i <= k; i++) {
            constCost += abs(i - m);
        }
    
        ll ans = best - constCost;
        cout << ans << "\n";
    }
    return 0;
}

// Solved!