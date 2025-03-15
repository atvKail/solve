#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int n, m;
    cin >> n >> m;
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; i++){
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
     
    vector<int> t(n + 1);
    for (int i = 1; i <= n; i++){
        cin >> t[i];
    }

    vector<int> order(n);
    for (int i = 0; i < n; i++){
        order[i] = i + 1;
    }

    sort(order.begin(), order.end(), [&](int a, int b){
        if(t[a] == t[b])
            return a < b;
        return t[a] < t[b];
    });
     
    vector<int> pos(n + 1);
    for (int i = 0; i < n; i++){
        pos[order[i]] = i;
    }
 
    for (int v : order){
        vector<bool> used(t[v] + 1, false);
        for (int u : g[v]){
             
            if (pos[u] < pos[v]){
                int topic_u = t[u];
                if(topic_u <= t[v])
                    used[topic_u] = true;
            }
        }
         
        for (int x = 1; x < t[v]; x++){
            if (!used[x]){
                cout << -1;
                return 0;
            }
        }
         
        if(used[t[v]]){
            cout << -1;
            return 0;
        }
    }

    for (int v : order)
        cout << v << " ";
    cout << "\n";
    return 0;
}
