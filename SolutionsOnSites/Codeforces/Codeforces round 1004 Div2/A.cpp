#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while(t--){
        int x, y;
        cin >> x >> y;
        
        int diff = x + 1 - y;
        if(diff >= 0 && diff % 9 == 0)
            cout << "Yes\n";
        else
            cout << "No\n";
    }
    return 0;
}
