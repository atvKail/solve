

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
#define forn(l, n) for (int i = l; i < n; i++)
#define all(a) a.begin(), a.end()
using ll = long long;
 
const int BITS = 31;
 
struct TrieNode {
    TrieNode* ch[2] = {nullptr, nullptr};
    int cnt = 0;
};
 
void insert(TrieNode* root, int x) {
    TrieNode* node = root;
    for (int i = BITS; i >= 0; i--) {
        int b = (x >> i) & 1;
        if (!node->ch[b]) node->ch[b] = new TrieNode();
        node = node->ch[b];
        node->cnt++;
    }
}
 
void erase(TrieNode* root, int x) {
    TrieNode* node = root;
    for (int i = BITS; i >= 0; i--) {
        int b = (x >> i) & 1;
        node = node->ch[b];
        node->cnt--;
    }
}
 
int getMaxXor(TrieNode* root, int x) {
    TrieNode* node = root;
    if (!node) return -1;
    int res = 0;
    for (int i = BITS; i >= 0; i--) {
        int b = (x >> i) & 1;
        if (node->ch[b ^ 1] && node->ch[b ^ 1]->cnt > 0) {
            res |= (1 << i);
            node = node->ch[b ^ 1];
        } else {
            node = node->ch[b];
        }
    }
    return res;
}
 
bool check(const vector<int>& a, int k, int m) {
    TrieNode* root = new TrieNode();
    for (int i = 0; i < m; i++) insert(root, a[i]);
    for (int i = 0; i < m; i++) {
        if (getMaxXor(root, a[i]) >= k) return true;
    }
    for (int i = m; i < a.size(); i++) {
        erase(root, a[i - m]);
        insert(root, a[i]);
        for (int j = i - m + 1; j <= i; j++) {
            if (getMaxXor(root, a[j]) >= k) return true;
        }
    }
    return false;
}
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int t; cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        vector<int> a(n);
        forn(0, n) cin >> a[i];
 
        if (k == 0) {
            cout << 1 << "\n";
            continue;
        }
        if (n == 1) {
            cout << -1 << "\n";
            continue;
        }
 
        int l = 2, r = n, res = -1;
        while (l <= r) {
            int m = (l + r) / 2;
            if (check(a, k, m)) {
                res = m;
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        cout << res << "\n";
    }
    return 0;
}
// 11 test TL