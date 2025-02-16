#include <bits/stdc++.h>
using namespace std;

bool contains7(long long x) {
    while(x > 0) {
        if(x % 10 == 7) return true;
        x /= 10;
    }
    return false;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while(t--){
        long long n;
        cin >> n;
        if(contains7(n)){
            cout << 0 << "\n";
            continue;
        }
        int ans = -1;
        const int max_m = 110; 
        
        for (int m = 1; m <= max_m; m++){
            long long N = n - m;
            if(N < 0) {
                continue;
            }
            vector<int> digits;
            long long temp = N;
            if(temp == 0){
                digits.push_back(0);
            } else {
                while(temp > 0){
                    digits.push_back(temp % 10);
                    temp /= 10;
                }
            }
            int L = digits.size();    
            int D = L + 1;            
            int maxCarry = 110;

            vector<vector<vector<int>>> dp(D+1, vector<vector<int>>(m+1, vector<int>(maxCarry, 0)));

            int d0 = (L > 0 ? digits[0] : 0);
            int s0 = d0; 
            int digit0 = s0 % 10;
            int carry0 = s0 / 10;
            
            int initFlag = (digit0 == 7) ? 2 : 1;
            if(carry0 < maxCarry){
                dp[1][0][carry0] |= initFlag;
            }
            for (int pos = 1; pos < D; pos++){
                int dcur = (pos < L ? digits[pos] : 0);
                for (int used = 0; used <= m; used++){
                    for (int carry = 0; carry < maxCarry; carry++){
                        int mask = dp[pos][used][carry];
                        if(mask == 0) {
                            continue;
                        }
                        for (int x = 0; x <= m - used; x++){
                            int new_used = used + x;
                            int sum_val = dcur + x + carry;
                            int new_digit = sum_val % 10;
                            int new_carry = sum_val / 10;
                            if(new_carry >= maxCarry) {
                                continue;
                            }

                            int new_mask = 0;
                            if(mask & 2) {
                                new_mask |= 2;
                            }
                            if((mask & 1) && new_digit != 7) {
                                new_mask |= 1;
                            }
                            if(new_digit == 7) {
                                new_mask |= 2;
                            }
                            dp[pos+1][new_used][new_carry] |= new_mask;
                        }
                    }
                }
            }
            if(dp[D][m][0] & 2){
                ans = m;
                break;
            }
        }
        if(ans == -1) {
            ans = max_m;
        }
        cout << ans << "\n";
    }
    return 0;
}
