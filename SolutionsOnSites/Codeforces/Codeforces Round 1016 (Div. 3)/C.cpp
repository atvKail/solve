#include <iostream>
#include <cmath>
using namespace std;

#define forn(l, n) for (int i = l; i < n; i++)
#define all(a) a.begin(), a.end()
using ll = long long;
using ld = long int;

bool isPrime(int x) {
    if(x < 2) {return false;}
    if(x == 2) {return true;}
    if(x % 2 == 0) {return false;}
    int r = sqrt(x);
    for (int i = 3; i <= r; i += 2)
        if(x % i == 0) {
            return false;
        }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int x, k;
        cin >> x >> k;

        if(k == 1) {
            cout << (isPrime(x) ? "YES" : "NO") << "\n";
            continue;
        }
        if(x != 1) {
            cout << "NO" << "\n";
            continue;
        }

        cout << ((k == 2) ? "YES" : "NO") << "\n";
    }
    return 0;
}
