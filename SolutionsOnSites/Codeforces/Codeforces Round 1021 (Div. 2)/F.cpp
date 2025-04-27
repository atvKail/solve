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
using vl = vector<ll>;
using vvi = vector<vi>;
using vvl = vector<vl>;

bool isPowerOfTwo(int n){
    return (n > 0) && ((n & (n - 1)) == 0);
}

bool canTransform(string s, string t, int n){
    if(isPowerOfTwo(n)){
        bool s_has_one = s.find('1') != string::npos;
        bool t_has_one = t.find('1') != string::npos;
        return (s_has_one && t_has_one) || (!s_has_one && !t_has_one);
    } else{
        int m = n / 2;
        string s_x = s.substr(0, m);
        string s_y = s.substr(m, m);
        string t_x = t.substr(0, m);
        string t_y = t.substr(m, m);
        if(m % 2 == 1){
            bool s_x_has_one = s_x.find('1') != string::npos;
            bool s_y_has_one = s_y.find('1') != string::npos;
            bool t_x_has_one = t_x.find('1') != string::npos;
            bool t_y_has_one = t_y.find('1') != string::npos;
            return (s_x_has_one == t_x_has_one) && (s_y_has_one == t_y_has_one);
        } else{
            return canTransform(s_x, t_x, m) && canTransform(s_y, t_y, m);
        }
    }
}

int main(){
    int t;
    cin >> t;
    while (t--){
        int n;
        string s, t;
        cin >> n >> s >> t;
        if(canTransform(s, t, n)){
            cout << "Yes" << endl;
        } else{
            cout << "No" << endl;
        }
    }
    return 0;
}

// WA 1