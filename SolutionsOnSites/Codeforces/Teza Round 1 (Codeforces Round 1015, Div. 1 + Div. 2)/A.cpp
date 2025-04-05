#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        if(n % 2 == 0){
            cout << -1 << endl;
            continue;
        }
        vector<int> p;
        p.push_back(n);
        p.push_back(2);
        p.push_back(1);
        for (int i = 3; i < n; i++){
            p.push_back(i);
        }
        for (int x : p) {
            cout << x << " ";
        }
        cout << endl;
    }
    return 0;
}
