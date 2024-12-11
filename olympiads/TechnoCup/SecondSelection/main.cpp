// #include <iostream>
// #include <vector>
// #include <algorithm>

// using namespace std;

// int main() {
//     int m;
//     cin >> m;
//     string number;
//     cin >> number;

//     bool has_even = false;
//     int sum = 0;
//     for (char d : number) {
//         int digit = d - '0';
//         sum += digit;
//         if (digit % 2 == 0) {
//             has_even = true;
//         }
//     }
//     if (!has_even || sum % 3 != 0) {
//         cout << -1 << endl;
//         return 0;
//     }
//     int swaps = 0;
//     for (int i = m - 1; i >= 0; --i) {
//         if ((number[i] - '0') % 2 == 0) {
//             for (int j = i; j < m - 1; ++j) {
//                 swap(number[j], number[j + 1]);
//                 swaps++;
//             }
//             cout << swaps << endl;
//             return 0;
//         }
//     }
//     cout << -1 << endl;
//     return 0;
// }                        // task A 100

