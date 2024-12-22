// #include <iostream>
// #include <vector>
// #include <unordered_map>
// using namespace std;


// int main() {
//     int n, b;
//     cin >> n >> b;
    
//     vector<int> a(n);
//     for (int i = 0; i < n; ++i) {
//         cin >> a[i];
//     }

//     long long ans = 0;
//     vector<int> bit_counts(1 << b);

//     unordered_map<int, int> cnt_global;

//     for (int k = 0; k < n; ++k) {
//         int ak = a[k];
//         unordered_map<int, int> cnt_pairs;

//         for (int i = 0; i < k; ++i) {
//             int ai = a[i];
//             int aj = ak - ai;

//             if (aj >= 0 && aj < (1 << b)) {
//                 if ((ai & aj) == 0 && __builtin_popcount(ai) + __builtin_popcount(aj) == b) {
//                     ans += cnt_pairs[aj];
//                 }
//             }

//             cnt_pairs[ai]++;
//         }
//     }

//     cout << ans << endl;
//     return 0;
// }

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, b;
    cin >> n >> b;
    vector<int> a(n);
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }

    vector<int> bit_counts(n);
    for(int i = 0; i < n; i++){
        bit_counts[i] = __builtin_popcount(a[i]);
    }

    unordered_map<int, int> cnt_pairs;
    cnt_pairs.reserve(n);
    cnt_pairs.max_load_factor(0.7f);

    long long ans = 0;

    for(int j = n - 1; j >= 0; j--){
        for(int i = 0; i < j; i++){
            if( (a[i] & a[j]) == 0 && bit_counts[i] + bit_counts[j] == b ){
                int sum = a[i] + a[j];
                auto itr = cnt_pairs.find(sum);
                if(itr != cnt_pairs.end()){
                    ans += itr->second;
                }
            }
        }
        cnt_pairs[a[j]]++;
    }

    cout << ans << endl;
    return 0;
}               // На 44 балла закрыта задача D
