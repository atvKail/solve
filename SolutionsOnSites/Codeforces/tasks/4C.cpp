#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    unordered_map<string, int> regss;

    while(n--) {
        string nme;
        cin >> nme;
        if (regss.find(nme) == regss.end()) {
            cout << "OK" << "\n";
            regss[nme] = 0;
        } else {
            int cnt = regss[nme];
            cnt++;
            string nnme = nme + to_string(cnt);
            while(regss.find(nnme) != regss.end()){
                cnt++;
                nnme = nme + to_string(cnt);
            }
            regss[nme] = cnt;
            regss[nnme] = 0;
            cout << nnme << "\n";
        }
    }
    return 0;
}
