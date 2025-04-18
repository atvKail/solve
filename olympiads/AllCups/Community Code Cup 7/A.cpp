#include <iostream>
#include <string>
#include <cctype>
using namespace std;

#define forn(l, n) for (int i = l; i < n; i++)
#define all(a) a.begin(), a.end()
#define f first
#define s second
using ll = long long;
using ld = long double;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    bool hasS = false, hasW = false, hasO = false, hasT = false;
    string str;

    forn(0, n) {
        cin >> str;
        for (char c : str) {
            char u = toupper(c);
            if (u == 'S') hasS = true;
            if (u == 'W') hasW = true;
            if (u == 'O') hasO = true;
            if (u == 'T') hasT = true;
        }
    }

    cout << (hasS && hasW && hasO && hasT ? "YES" : "NO") << "\n";
    return 0;
}
