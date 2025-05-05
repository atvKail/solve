#include <bits/stdc++.h>
using namespace std;

#define forn(i, l, r) for(int i = l; i < r; ++i)
#define all(a) (a).begin(), (a).end()
#define f first
#define s second
#define pb push_back
#define mp make_pair

using ll = long long;
using pii = pair<int, int>;
using vi = vector<int>;
using vb = vector<bool>;
using vvi = vector<vi>;
using unomapss = unordered_map<string, string>;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    int q;
    cin >> q;
    unomapss cur2orig;
    unomapss orig2cur;
    forn(i, 0, q){
        string oldh, newh;
        cin >> oldh >> newh;

        string orig;
        auto it = cur2orig.find(oldh);
        if(it != cur2orig.end()){
            orig = it->s;
            cur2orig.erase(it);
        } else{
            
            orig = oldh;
        }
        cur2orig[newh] = orig;
        orig2cur[orig] = newh;
    }

    int n = orig2cur.size();
    cout << n << "\n";
    
    for(auto &p : orig2cur){
        cout << p.f << " " << p.s << "\n";
    }
    return 0;
}
