#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <algorithm>
using namespace std;

#define forn(i, l, r) for(int i = l; i < r; ++i)
#define all(a) (a).begin(), (a).end()
#define f first
#define s second

using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string you;
    int n;
    cin >> you >> n;

    map<string, ll> score;
    set<string> names;

    forn(i, 0, n){
        string X, act;
        cin >> X >> act;

        ll val;
        string YwithS, tmp, dummy;
        if(act == "posted"){
            val = 15;
            cin >> tmp >> YwithS >> dummy;
        } else if(act == "commented"){
            val = 10;
            cin >> tmp >> YwithS >> dummy;
        } else{ // is Likes
            val = 5;
            cin >> YwithS
                >> dummy;
        }

        string Y = YwithS.substr(0, YwithS.size() - 2);
        if(X != you) names.insert(X);
        if(Y != you) names.insert(Y);

        if(X == you && Y != you){
            score[Y] += val;
        } else if(Y == you && X != you){
            score[X] += val;
        }
    }

    vector<string> res(all(names));
    sort(all(res), [&](const string &a, const string &b){
        ll sa = score.count(a) ? score[a] : 0;
        ll sb = score.count(b) ? score[b] : 0;
        if(sa != sb) return sa > sb;
        return a < b;
    });

    for(auto &name : res){
        cout << name << "\n";
    }
    return 0;
}
