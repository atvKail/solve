#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
#define forn(l, n) for (int i = l; i < n; i++)
#define all(a) a.begin(), a.end()
using ll = long long;
 
const int MAXCAND = 128;
 
vector<int> mergeCand(const vector<int>& a, const vector<int>& b) {
    int szA = a.size(), szB = b.size();
    vector<int> merged;
    merged.reserve(szA + szB);
 
    int i = 0, j = 0;
    while(i < szA && j < szB) {
        if(a[i] < b[j]) {
            merged.push_back(a[i++]);
        } else {
            merged.push_back(b[j++]);
        }
    }
 
    while(i < szA) {
        merged.push_back(a[i++]);
    }
    while(j < szB) {
        merged.push_back(b[j++]);
    }
 
    int take = MAXCAND / 2;
    vector<int> res;
    int total = merged.size();
    forn (0, min(take, total)){
        res.push_back(merged[i]);
    }
 
    forn (max(0, total - take), total) {
        res.push_back(merged[i]);
    }
 
    if (res.size() > MAXCAND) {
        res.resize(MAXCAND);
    }
    return res;
}
 
int getMaxXor(const vector<int>& cand) {
    int res = 0, sz = cand.size();
    forn(0, sz) {
        for (int j = i + 1; j < sz; j++) {
            res = max(res, cand[i] ^ cand[j]);
        }
    }
    return res;
}
 
struct SegTree {
    private:
        int n;
        vector<vector<int>> tree;
    public:
        SegTree(const vector<int>& arr) {
            n = arr.size();
            tree.resize(4 * n);
            build(arr, 1, 0, n - 1);
        }
 
        void build(const vector<int>& arr, int idx, int l, int r) {
            if(l == r) {
                tree[idx] = { arr[l] };
                return;
            }
            int mid = (l + r) / 2;
            build(arr, 2 * idx, l, mid);
            build(arr, 2 * idx + 1, mid + 1, r);
            tree[idx] = mergeCand(tree[2 * idx], tree[2 * idx + 1]);
        }
 
        vector<int> query(int idx, int l, int r, int ql, int qr) {
            if(ql > r || qr < l) {
                return {};
            }
            if(ql <= l && r <= qr) {
                return tree[idx];
            }
 
            int mid = (l + r) / 2;
            vector<int> lr = query(2 * idx, l, mid, ql, qr);
            vector<int> rr = query(2 * idx + 1, mid + 1, r, ql, qr);
            if(lr.empty()) {
                return rr;
            }
            if(rr.empty()) {
                return lr;
            }
            return mergeCand(lr, rr);
        }
 
        vector<int> query(int l, int r) {
            return query(1, 0, n - 1, l, r);
        }
};
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;
 
        vector<int> a(n);
        forn(0, n) cin >> a[i];
 
        if(k == 0) {
            cout << 1 << "\n";
            continue;
        }
        if(n == 1) {
            cout << -1 << "\n";
            continue;
        }
 
        SegTree seg(a);
 
        int res = -1;
        int l = 2, r = n;
        while(l <= r) {
            int m = l + (r - l) / 2;
            bool f = false;
            forn (0, n - m + 1) {
                vector<int> cand = seg.query(i, i + m - 1);
                if(getMaxXor(cand) >= k) {
                    f = true;
                    break;
                }
            }
            if(f) {
                res = m;
                r = m - 1; 
            }
            else {
                l = m + 1;
            }
        }
        cout << res << "\n";
    }
    return 0;
}