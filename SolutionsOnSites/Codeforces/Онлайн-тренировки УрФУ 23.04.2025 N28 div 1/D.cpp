#include <iostream>
#include <vector>
using namespace std;

#define forn(i, l, r) for(int i = l; i < r; ++i)
#define all(a) (a).begin(), (a).end()
#define f first
#define s second

using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    // Сфен до ~2e5
    int S = max(200000, n + 10);
    vector<bool> is_prime(S + 1, true);
    is_prime[0] = is_prime[1] = false;
    for(int i = 2; i * i <= S; ++i) if(is_prime[i]){
        for(int j = i * i; j <= S; j += i)
            is_prime[j] = false;
    }

    int start = max(2, n - 1);
    int P = start;
    while(P <= S && !is_prime[P]) ++P;

    ll dlt = (ll)P - (n - 1LL);

    cout << P << " " << P << "\n";
    cout << 1 << " " << 2 << " " << (1 + dlt) << "\n";
    forn(u, 2, n){
        cout << u << " " << (u + 1) << " " << 1 << "\n";
    }

    int need = m - (n - 1);
    const int bg = (int)1e9;
    int i = 1, j = 3;
    while(need--){
        if(j > n){
            ++i;
            j = i + 2;
        }
        cout << i << " " << j << " " << bg << "\n";
        ++j;
    }
    return 0;
}
