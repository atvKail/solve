// #include <vector>
// #include <iostream>
// using namespace std;

// #pragma GCC optimize("O3,unroll-loops")

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);
    
//     int n;
//     cin >> n;
//     vector<int> a(n);
//     for (int &x : a) cin >> x;
    
//     vector<int> suffmin(n);
//     suffmin[n - 1] = a[n - 1];
//     for (int i = n - 2; i >= 0; --i) {
//         suffmin[i] = min(a[i], suffmin[i + 1]);
//     }
    
//     int q;
//     cin >> q;
//     vector<int> result;
//     result.reserve(q);
    
//     while (q--) {
//         int l, x;
//         cin >> l >> x;
//         int cnt = 0, curritems = x;
//         for (int i = l - 1; i < n; ++i) {
//             if (curritems >= a[i]) {
//                 ++cnt;
//                 --curritems;
//             } else {
//                 break;
//             }
//         }
//         result.push_back(cnt);
//     }
    
//     for (int res : result) {
//         cout << res << "\n";
//     }
    
//     return 0;
// }

#include <iostream>
#include <vector>
using namespace std;

#pragma GCC optimize("O3,unroll-loops")

int n;
vector<int> G;
vector<int> seg;

void build(int idx, int l, int r) {
    if (l == r) {
        seg[idx] = G[l];
        return;
    }
    int mid = (l + r) / 2;
    build(idx * 2, l, mid);
    build(idx * 2 + 1, mid + 1, r);
    seg[idx] = max(seg[idx * 2], seg[idx * 2 + 1]);
}

int find_first(int idx, int l, int r, int ql, int qr, int threshold) {
    if (r < ql || l > qr)
        return -1;
        
    if (seg[idx] <= threshold)
        return -1;

    if (l == r)
        return l;
    
    int mid = (l + r) / 2;
    int leftAns = find_first(idx * 2, l, mid, ql, qr, threshold); //эт левый подотрезок

    if (leftAns != -1)
        return leftAns;

    return find_first(idx * 2 + 1, mid + 1, r, ql, qr, threshold); // Правый подотрезок
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    
    G.resize(n);
    for (int i = 0; i < n; i++){
        G[i] = a[i] + i;
    }
    
    seg.resize(4 * n);
    build(1, 0, n - 1);
    
    int q;
    cin >> q;
    while(q--){
        int l, x;
        cin >> l >> x;
        int offset = l - 1;
        int threshold = x + offset;

        if (G[offset] > threshold) {
            cout << 0 << "\n";
            continue;
        }

        int pos = find_first(1, 0, n - 1, offset, n - 1, threshold);
        int ans;
        if (pos == -1)
            ans = n - offset;
        else
            ans = pos - offset;
        cout << ans << "\n";
    }
    
    return 0;
}
