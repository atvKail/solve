#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1000000007;
const int N = 5050;

long long fac[N], C[N][N], d[N][N];
bool vis[N];

void init() {
    fac[0] = 1;
    for (int i = 1; i < N; i++) {
        fac[i] = (fac[i-1] * i) % MOD;
    }
    for (int i = 0; i < N; i++) {
        C[i][0] = C[i][i] = 1;
        for (int j = 1; j < i; j++) {
            C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    init();
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        
        vector<int> a(n + 1), b(n + 1);
        for (int i = 0; i <= n; i++) {
            vis[i] = 0;
            for (int j = 0; j <= n; j++) {
                d[i][j] = 0;
            }
        }
        
        for (int i = 1; i <= n; i++) {
            cin >> a[i];
            b[i] = b[i-1] + (a[i] == -1);
            if (a[i] != -1) {
                vis[a[i]] = 1;
            }
        }
        
        int mn1 = n;
        for (int i = 1; i <= n; i++) {
            int mn2 = n;
            for (int j = n; j >= i; j--) {
                int x = b[j] - b[i-1], y = min(mn1, mn2);
                d[x][0]++;
                d[x][y]--;
                if (a[j] != -1) {
                    mn2 = min(mn2, a[j]);
                }
            }
            if (a[i] != -1) {
                mn1 = min(mn1, a[i]);
            }
        }
        
        for (int i = 0; i <= b[n]; i++) {
            for (int j = 1; j <= n; j++) {
                d[i][j] += d[i][j-1];
            }
        }
        
        long long ans = 0;
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            cnt += (!vis[i]);
            for (int j = cnt; j <= b[n]; j++) {
                ans = (ans + ((C[j][cnt] * fac[cnt]) % MOD * fac[b[n] - cnt] % MOD * d[j][i])) % MOD;
            }
        }
        cout << ans << '\n';
    }
    return 0;
} 

// Solved!