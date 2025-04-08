#include <iostream>
#include <string>
using namespace std;

#define forn(l, n) for (int i = l; i < n; i++)
#define all(a) a.begin(), a.end()
using ll = long long;
using ld = long int;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        string n;
        cin >> n;

        int l = n.size(), zeros = 0, best = 0;
        forn(0, l){
            if(n[i] != '0'){
                int cand = zeros + 1;
                if(cand > best)
                    best = cand;
            }
            if(n[i] == '0')
                zeros++;
        }
        cout << (l - best) << "\n";
    }
    return 0;
}
