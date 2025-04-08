#include <iostream>
using namespace std;

#define forn(l, n) for (int i = l; i < n; i++)
#define all(a) a.begin(), a.end()
#define f first
#define s second
using ll = long long;
using ld = long int;

ll getN(int n, int x, int y) {
    if(n == 1) {
        if(x == 1 && y == 1) return 1;
        if(x == 1 && y == 2) return 4;
        if(x == 2 && y == 1) return 3;
        if(x == 2 && y == 2) return 2;
    }
    int hf = 1 << (n - 1);
    ll S = (ll)hf * hf, oft = 0, sb;
    if(x <= hf && y <= hf) {
        sb = getN(n - 1, x, y);
        oft = 0;
    } else if(x > hf && y > hf) {
        sb = getN(n - 1, x - hf, y - hf);
        oft = S;
    } else if(x > hf && y <= hf) {
        sb = getN(n - 1, x - hf, y);
        oft = 2 * S;
    } else {
        sb = getN(n - 1, x, y - hf);
        oft = 3 * S;
    }
    return oft + sb;
}

pair<int,int> getCoords(int n, ll d) {
    if(n == 1) {
        if(d == 1) return {1, 1};
        if(d == 4) return {1, 2};
        if(d == 3) return {2, 1};
        if(d == 2) return {2, 2};
    }
    int hf = 1 << (n - 1);
    ll S = (ll)hf * hf;

    int qdt = (d - 1) / S;
    ll r = (d - 1) % S, subd = r + 1;

    pair<int,int> sb = getCoords(n - 1, subd);

    int x, y;
    if(qdt == 0) {x = sb.f; y = sb.s;}
    else if(qdt == 1) {
        x = sb.f + hf;
        y = sb.s + hf;
    }
    else if(qdt == 2) {
        x = sb.f + hf;
        y = sb.s;
    }
    else {
        x = sb.f;
        y = sb.s + hf;
    }
    return {x, y};
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while(t--){
        int n, t;
        cin >> n >> t;

        while(t--){
            string op;
            cin >> op;

            if(op == "->") {
                int x, y;
                cin >> x >> y;

                cout << getN(n, x, y) << "\n";
            } else {
                ll d;
                cin >> d;

                pair<int,int> p = getCoords(n, d);
                cout << p.f<< " " << p.s << "\n";
            }
        }
    }
    return 0;
}
