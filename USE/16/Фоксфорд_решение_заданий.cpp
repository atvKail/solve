// #include <iostream>
// using namespace std;

// long long F(int n, long long total = 0) {
//     total += 2 * n + 1;
//     if (n > 1) {
//         total += 3 * n - 8;
//         total = F(n - 1, total);
//         total = F(n - 4, total);
//     }
//     return total;
// }

// pair<int, long long> find_minimum_n() {
//     int n = 1;
//     while (true) {
//         long long total = F(n);
//         if (total > 5000000) {
//             return make_pair(n, total);
//         }
//         n++;
//     }
// }

// int main() {
//     pair<int, long long> result = find_minimum_n();
//     cout << result.first << " " << result.second << endl;
//     return 0;
// }
// #include <iostream>
// using namespace std;

// long long F(int n) {
//     if (n < 3) return 1;
//     if (n % 2 == 0) return (n * (n + 2)) / 2 + 1;
//     return F(n - 1) - 2;
// }

// int main() {
//     cout << F(2554) - F(2544) << endl;
//     return 0;
// }
