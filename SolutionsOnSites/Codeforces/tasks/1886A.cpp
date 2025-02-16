#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        long long n;
        cin >> n;
        if(n < 7) {
            cout << "NO" << "\n";
        } else {
            if(n % 3 != 0) {
                cout << "YES" << "\n";
                cout << 1 << " " << 2 << " " << n - 3 << "\n";
            } else {
                if(n == 9) {
                    cout << "NO" << "\n";
                } else {
                    cout << "YES" << "\n";
                    cout << 1 << " " << 4 << " " << n - 5 << "\n";
                }
            }
        }
    }
    return 0;
}
