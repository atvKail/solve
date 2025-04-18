#include <iostream>
#include <vector>
using namespace std;

#define forn(i,l,r) for (int i = l; i < r; ++i)
#define all(a) a.begin(), a.end()
#define f first
#define s second
using ll = long long;
const int MOD = 1000000007;

int gcd(int a, int b) {
    return b ? gcd(b, a % b) : a;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<ll> fact(n + 1,1);
    forn(i, 1, n + 1){
        fact[i] = fact[i - 1] * i % MOD;
    }

    ll res = 0;
    int N = 1 << n;
    forn(mask, 1, N){
        int elms[20], m = 0;
        forn(idx, 0, n){
            if (mask & (1 << idx))
                elms[m++] = idx + 1;
        }
        int g = elms[0];
        forn(k, 1, m){
            g = gcd(g, elms[k]);
            if (g == 1) break;
        }
        if (g > 1) continue;

        int kv = 0;
        if (mask & 1){
            kv = 1;
        } else {
            bool fnd2 = false;
            forn(a, 0, m){
                if (fnd2) break;
                forn(b, a + 1, m){
                    if (gcd(elms[a], elms[b]) == 1){
                        kv = 2;
                        fnd2 = true;
                        break;
                    }
                }
            }
            if(!fnd2) {
                bool fnd3 = false;
                forn(a, 0, m) {
                    if(fnd3) break;
                    forn(b, a + 1, m){
                        int g2 = gcd(elms[a], elms[b]);
                        forn(c, b + 1, m){
                            if(gcd(g2, elms[c]) == 1) {
                                kv = 3;
                                fnd3 = true;
                                break;
                            }
                        }
                        if(fnd3) break;
                    }
                }
                if (!fnd3) kv = m;
            }
        }
        res = (res + kv * fact[m] % MOD * fact[n - m] % MOD) % MOD;
    }

    cout << res << "\n";
    return 0;
}
