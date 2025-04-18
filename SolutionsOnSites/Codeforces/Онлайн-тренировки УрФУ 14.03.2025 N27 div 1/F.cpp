#include <iostream>
#include <string>
using namespace std;

#define forn(i, a, b) for (int i = a; i < b; i++)
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    cin >> n;
    cin >> s;

    int ones = 0, zeros = 0;
    forn (i, 0, n) {
        if (s[i] == '1') ones++;
        else zeros++;
    }
    int tot = 1 << n;
    int low = 1 << ones;
    int high = tot - ((zeros > 0) ? (1 << zeros) : 1) + 1;
    for (int i = low; i <= high; i++) cout << i << " ";
    cout << "\n";
    return 0;
}
