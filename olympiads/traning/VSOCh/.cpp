// #include <bits\stdc++.h>
// using namespace std;

// class SegmentTree{
// private:
//     int n;
//     vector<int> arr;
//     vector<int> tree;

//     void build(int v, int tl, int tr) {
//         if (tl == tr) {
//             tree[v] = arr[tl];
//         } else {
//             int tm = tl + (tr - tl) / 2;
//             build(2 * v, tl, tm);
//             build(2 * v + 1, tm + 1, tr);
//             tree[v] = tree[2 * v] + tree[2 * v + 1];
//         }
//     }
// public:
//     // vector<int> tree;
//     SegmentTree(const vector<int> &InputArr){
//         n = InputArr.size();
//         arr = InputArr;
//         tree.resize(4 * n);
//         build(1, 0, arr.size() - 1);
//     }

//     void update(int v, int tl, int tr, int pos, int x){
//         tree[v] += x; // Любая операция
//         if (tl == tr){
//             // tree[v] = x;
//             return;
//         }
//         int tm = tl + (tr - tl) / 2;
//         if (pos < tm){
//             update(2 * v, tl, tm, pos, x);
//         }
//         else{
//             update(2 * v + 1, tm + 1, tr, pos, x);
//         }
//         // tree[v] = tree[2 * v] + tree[2 * v + 1];
//     }

//     int getSum(int v, int tl, int tr, int l, int r){
//         if (tl == l && tr == r){
//             return tree[v];
//         }
//         cout << v;
//         int result = 0;
//         int tm = tl + (tr - tl) / 2;
//         if (l <= tm){
//             result += getSum(2 * v, tl, tm, l, min(r, tm)); // Любая операция
//         }
//         if (r > tm){
//             result += getSum(2 * v + 1, tm + 1, tr, max(l, tm + 1), r); // Любая операция
//         }
//         return result;
//     }
// };



///////////// https://informatics.msk.ru/mod/statements/view.php?chapterid=111253#1
// #include <bits/stdc++.h>

// using namespace std;

// struct Node {
//     int x, h;
//     Node(int x, int h): x(x), h(h) {};
// };

// int main(){
//     int n;
//     long long ans = 0;
//     cin >> n;

//     stack<Node> stck;

//     stck.push(Node(0, -1));

//     for (int i = 1; i <= n + 1; i++) {
//         int h, x = i;

//         if (i <= n) {
//             cin >> h;
//         }
//         else {
//             h = 0;
//         }

//         while (h <= stck.top().h) {
//             x = stck.top().x;
//             int hp = stck.top().h;
//             long long area = 1LL * hp * (i - x);

//             ans = max(area, ans);

//             stck.pop();
//         }
//         stck.push(Node(x, h));
//     }

//     cout << ans;
// }
///////////////////// https://informatics.msk.ru/mod/statements/view.php?chapterid=756#1
// 3583
// #include <bits/stdc++.h>

// using namespace std;

// int main() {
//     int n, k;
//     cin >> n >> k;
//     vector<int> arr(n);

//     for (int i = 0; i < n; i++) {
//         cin >> arr[i];
//     }

//     deque<int> dq;

//     for (int i = 0; i < arr.size(); i++) {
//         if (!dq.empty() && dq.front() <= i - k) {
//             dq.pop_front();
//         }

//         while (!dq.empty() && arr[dq.back()] >= arr[i]) {
//             dq.pop_back();
//         }

//         dq.push_back(i);

//         if (i >= k - 1) {
//             cout << arr[dq.front()] << endl;
//         }
//     }
//     return 0;
// }
///////////////// https://acmp.ru/asp/champ/index.asp?main=tasks&id_stage=44673 Задача I. Новый год в детском саду
// /*
// ░░░░░▄▀▀▀▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
// ▄███▀░PPPP░░░▌░ЗАПУСКАЕМ░МАГИЧКУ-PRAGMA░░░
// ████▌░░░░░▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
// ▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀(@)▀
// */

// #pragma GCC optimize("Ofast,unroll-loops")

// #include<iostream>

// using namespace std;

// using ll = long long;

// int main() {
//     ios_base::sync_with_stdio(0);
//     cin.tie(0); cout.tie(0);

//     int t;
//     cin >> t;
//     while (t--) {
//         ll n, a, b;
//         cin >> n >> a >> b;

//         ll fblocksx = a / n;
//         ll fblocksy = b / n;

//         ll remx = a % n + 1;
//         ll remy = b % n + 1;

//         ll totalWays = fblocksx * fblocksy * n; // ok

//         totalWays += remx * fblocksy;
//         totalWays += remy * fblocksx;

//         totalWays += max(0LL, b % n + a % n + 1 - n);

//         cout << totalWays << endl;
//     }
//     return 0;
// }
/////////////Задача B. Числовая лесенка
// #include <iostream>

// using namespace std;

// using ll = long long;

// int main(){
//     ll a, b, k;
//     cin >> a >> b >> k;

//     for (ll row = a; row <= b; ++row) {
//         ll start = row * (row - 1) / 2 + 1;;
//         ll cnt = min(k, row);
//         for (ll i = 0; i < cnt; ++i) {
//             if (i > 0) cout << " ";
//             cout << (start + i);
//         }
//         cout << "\n";
//     }
// }
// /////////Задача C. Площадь четырёхугольника
// #include <iostream>
// #include <iomanip>
// #include <sstream>

// using namespace std;

// int main(){
//     double x, y, z;
//     cin >> x >> y >> z;

//     stringstream ss;
//     ss <<fixed << setprecision(6) << z + y - x;

//     string result = ss.str();
//     size_t pos = result.find_last_not_of('0');
//     if (result[pos] == '.') {
//         result = result.substr(0, pos);
//     }

//     cout << result << endl;
// }

///////////////Задача D. Несократимые дроби
// #include <iostream>
// #include <vector>
// #include <algorithm>

// using namespace std;

// struct by_fract {
//     bool operator()(pair<int, int> const &a, pair<int, int> const &b) const {
//         return a.first * b.second < b.first * a.second;
//     }
// };

// int main() {
//     int n, p, q;
//     cin >> n >> p >> q;

//     vector<pair<int, int>> fractions;

//     for (int b = 1; b <= n; b++) {
//         int mina = b / p + 1;
//         int maxa = b / q;
//         if (mina > maxa) continue;

//         for (int a = mina; a <= maxa; a++) {
//             if (__gcd(a, b) == 1) {
//                 fractions.push_back(make_pair(a, b));
//             }
//         }
//     }

//     sort(fractions.begin(), fractions.end(), by_fract());

//     for (int i = 0; i < fractions.size() - 1; i++) {
//         cout << fractions[i].first << "/" << fractions[i].second << "\n";
//     }

//     return 0;
// }
//////////////Задача G. Прямоугольник - 2
// #include <iostream>
// using namespace std;

// int main(){
//     int x1, y1, x2, y2, x3, y3;

//     cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
//     int y4, x4;
//     if (((x2 - x1) * (x3 - x1) + (y2 - y1) * (y3 - y1)) == 0){
//         x4 = x3 + x2 - x1;
//         y4 = y3 + y2 - y1;
//     }
//     else if (((x1 - x2) * (x3 - x2) + (y1 - y2) * (y3 - y2)) == 0){
//         x4 = x3 + x1 - x2;
//         y4 = y3 + y1 - y2;
//     }
//     else if (((x1 - x3) * (x2 - x3) + (y1 - y3) * (y2 - y3)) == 0){
//         x4 = x2 + x1 - x3;
//         y4 = y2 + y1 - y3;
//     }
//     cout << x4 << " " << y4 << endl;
// }
