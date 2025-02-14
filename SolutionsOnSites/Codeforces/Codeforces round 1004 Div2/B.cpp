#include <bits/stdc++.h>
using namespace std;
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t; 
    cin >> t;
    while(t--){
        int n; 
        cin >> n;
        vector<int> arr(n);
        int mn = INT_MAX, mx = 0;
        for (int i=0; i<n; i++){
            cin >> arr[i];
            mn = min(mn, arr[i]);
            mx = max(mx, arr[i]);
        }
        int X_max = mx + n;
        vector<int> freq(X_max+1,0);
        for (int a : arr) {
            if(a <= X_max)
                freq[a]++;
        }
 
        int dmax = n; 
        vector<vector<bool>> dp(X_max+2, vector<bool>(dmax+1, false));
        dp[mn][0] = true;
 
        for (int x = mn; x <= X_max; x++){
            for (int d_prev = 0; d_prev <= dmax; d_prev++){
                if(!dp[x][d_prev]) continue;
                int avail = freq[x] + d_prev;
                for (int d = 0; d <= avail && d <= dmax; d++){
                    if( (d % 2) != (avail % 2) ) continue;
                    int F = avail - d;
                    if(d > 0 && F <= 0) continue;
                    if(x+1 <= X_max+1)
                        dp[x+1][d] = true;
                }
            }
        }
        if(dp[X_max+1][0])
            cout << "Yes\n";
        else
            cout << "No\n";
    }
    return 0;
}
