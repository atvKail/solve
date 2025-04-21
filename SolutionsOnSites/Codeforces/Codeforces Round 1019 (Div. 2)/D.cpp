#include <iostream>
#include <vector>
using namespace std;

#define forn(i, l, r) for (int i = l; i < r; ++i)
#define all(a) a.begin(), a.end()
#define f first
#define s second
using ll = long long;

vector<int> constrctPerm(const vector<int>& a){
    int n = a.size();
    vector<int> p(n, 0);
    vector<bool> used(n + 1, false);
    int root = -1;

    forn(i, 0, n){
        if(a[i] == -1){
            root = i;
            break;
        }
    }

    p[root] = n;
    used[n] = true;

    vector<int> stack = {root};
    int currv = n - 1;

    while (!stack.empty()){
        int idx = stack.back();
        stack.pop_back();
        int iter = a[idx];
        if(iter == -1) continue;

        forn(i, 0, n){
            if(a[i] == iter && !used[i + 1]){
                p[i] = currv--;
                used[p[i]] = true;
                stack.push_back(i);
            }
        }
    }

    forn(i, 0, n){
        if(p[i] == 0){
            while (used[currv]) --currv;
            p[i] = currv--;
            used[p[i]] = true;
        }
    }
    return p;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--){
        int n;
        cin >> n;
        
        vector<int> a(n);
        forn(i, 0, n) cin >> a[i];
        
        vector<int> p = constrctPerm(a);
        for (int val : p){
            cout << val << " ";
        }
        cout << "\n";
    }
    return 0;
}
// WA 1