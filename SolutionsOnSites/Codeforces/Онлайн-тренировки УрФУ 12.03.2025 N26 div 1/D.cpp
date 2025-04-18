#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define forn(i, a, b) for (int i = a; i < b; i++)
#define all(a) a.begin(), a.end()
using ll = long long;

struct Lecture {
    ll sa, ea, sb, eb;
};

struct SegTreeMax {
    int n;
    vector<ll> seg;
    SegTreeMax(const vector<ll>& arr) {
        n = arr.size();
        seg.resize(4 * n);
        build(arr, 1, 0, n - 1);
    }
    void build(const vector<ll>& arr, int idx, int l, int r) {
        if(l == r) { seg[idx] = arr[l]; return; }
        int mid = (l + r) / 2;
        build(arr, 2 * idx, l, mid);
        build(arr, 2 * idx + 1, mid + 1, r);
        seg[idx] = max(seg[2 * idx], seg[2 * idx + 1]);
    }
    ll query(int idx, int l, int r, int ql, int qr) {
        if(ql > r || qr < l) return -1e18;
        if(ql <= l && r <= qr) return seg[idx];
        int mid = (l + r) / 2;
        return max(query(2 * idx, l, mid, ql, qr), query(2 * idx + 1, mid + 1, r, ql, qr));
    }
    ll query(int l, int r) {
        return query(1, 0, n - 1, l, r);
    }
};

struct SegTreeMin {
    int n;
    vector<ll> seg;
    SegTreeMin(const vector<ll>& arr) {
        n = arr.size();
        seg.resize(4 * n);
        build(arr, 1, 0, n - 1);
    }
    void build(const vector<ll>& arr, int idx, int l, int r) {
        if(l == r) { seg[idx] = arr[l]; return; }
        int mid = (l + r) / 2;
        build(arr, 2 * idx, l, mid);
        build(arr, 2 * idx + 1, mid + 1, r);
        seg[idx] = min(seg[2 * idx], seg[2 * idx + 1]);
    }
    ll query(int idx, int l, int r, int ql, int qr) {
        if(ql > r || qr < l) return 1e18;
        if(ql <= l && r <= qr) return seg[idx];
        int mid = (l + r) / 2;
        return min(query(2 * idx, l, mid, ql, qr), query(2 * idx + 1, mid + 1, r, ql, qr));
    }
    ll query(int l, int r) {
        return query(1, 0, n - 1, l, r);
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    vector<Lecture> lec(n);
    forn(i, 0, n) {
        cin >> lec[i].sa >> lec[i].ea >> lec[i].sb >> lec[i].eb;
    }
    
    bool f = true;
    
    {
        vector<Lecture> v = lec;
        sort(all(v), [](const Lecture &A, const Lecture &B) {
            return A.sa < B.sa;
        });
        vector<ll> arrSb(n), arrEb(n), arrSa(n);
        forn(i, 0, n) {
            arrSb[i] = v[i].sb;
            arrEb[i] = v[i].eb;
            arrSa[i] = v[i].sa;
        }
        SegTreeMax segMaxSb(arrSb);
        SegTreeMin segMinEb(arrEb);
        forn(i, 0, n) {
            int pos = upper_bound(arrSa.begin() + i + 1, arrSa.end(), v[i].ea) - arrSa.begin();
            if(pos - (i+1) < 1) continue;
            ll maxSb = segMaxSb.query(i + 1, pos - 1);
            ll minEb = segMinEb.query(i + 1, pos - 1);
            if(maxSb > v[i].eb || minEb < v[i].sb) { f = false; break; }
        }
    }
    
    if(f) {
        vector<Lecture> v = lec;
        sort(all(v), [](const Lecture &A, const Lecture &B) {
            return A.sb < B.sb;
        });
        vector<ll> arrSa(n), arrEa(n), arrSb(n);
        forn(i, 0, n) {
            arrSa[i] = v[i].sa;
            arrEa[i] = v[i].ea;
            arrSb[i] = v[i].sb;
        }
        SegTreeMax segMaxSa(arrSa);
        SegTreeMin segMinEa(arrEa);
        forn(i, 0, n) {
            int pos = upper_bound(arrSb.begin() + i + 1, arrSb.end(), v[i].eb) - arrSb.begin();
            if(pos - (i + 1) < 1) continue;
            ll maxSa = segMaxSa.query(i + 1, pos - 1);
            ll minEa = segMinEa.query(i  +1, pos - 1);
            if(maxSa > v[i].ea || minEa < v[i].sa) { f = false; break; }
        }
    }
    
    cout << (f ? "YES" : "NO") << "\n";
    return 0;
}
