// # include <bits/stdc++.h>
// using namespace std;

// using ll = long long;
// #define MAX 1000000001


// int main() {
//     ll n, k;
//     cin >> n >> k;
//     vector<ll> a(n, 0);
//     for (ll i = 0; i < n; i++) {
//         cin >> a[i];
//     }
//     sort(a.begin(), a.end());

//     ll l = 0, r = n - 1;
//     while (l <= r) {
//         ll mid = l + (r - l) / 2;
//         if (a[mid] < k) {
//             l = mid + 1;
//         } else {
//             r = mid - 1;
//         }
//     }
//     cout << n -l;
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// class Solution {
// public:
//     int v[13] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
//     string r[13] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};

//     string intToRoman(int n) {
//         string ans = "";
//         for (int i = 0; n; i++){
//             while (n >= v[i]) {
//                 ans += r[i];
//                 n -= v[i];
//             }
//         }
//         return ans;
//     }
// };

// int main(){
//     int n;
//     cin >> n;
//     Solution s = Solution();
//     cout << s.intToRoman(n);
//     return 0;
// }  // LeetCode integer to roman


// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     char *s1, *s2;
//     int n, m, nn, mn;
//     cin >> s1;
//     cin >> s2;

//     n = (s1[0] - '0') * 10 + (s1[1] - '0');
//     m = (s1[3] - '0') * 10 + (s1[4] - '0');

//     nn = (s2[0] - '0') * 10 + (s2[1] - '0');
//     mn = (s2[3] - '0') * 10 + (s2[4] - '0');

//     if (mn - m < 0) {
//         printf("%02d:%02d\n", 24 - n + nn - 1, 60 + mn - m);
//     }
//     printf("%02d:%02d\n", 24 - n + nn, mn - m);
// }
