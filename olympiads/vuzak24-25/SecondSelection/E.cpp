#include <iostream>
#include <vector>
using namespace std;

#pragma GCC optimize("O3,unroll-loops")

using ll = long long;

void dfs_tree(const vector<vector<pair<int, ll>>>& graph, int s,
        vector<ll>& dist_s, vector<int>& par, vector<int>& tin, vector<int>& tout) {
    int n = graph.size();
    int timer = 0;
    vector<int> idx(n, 0);
    vector<int> st;
    st.reserve(n);
    st.push_back(s);
    par[s] = -1;
    while (!st.empty()) {
        int v = st.back();
        if (idx[v] == 0)
            tin[v] = timer++;
        if (idx[v] < (int)graph[v].size()) {
            auto edge = graph[v][idx[v]++];
            int nv = edge.first;
            ll w = edge.second;
            if (nv == par[v])
                continue;
            par[nv] = v;
            dist_s[nv] = dist_s[v] + w;
            st.push_back(nv);
        } else {
            tout[v] = timer++;
            st.pop_back();
        }
    }
}

void compute_dist_t(const vector<vector<pair<int, ll>>>& graph, int t,
        vector<ll>& dist_t) {
    int n = graph.size();
    vector< pair<int, int> > dstack;
    dstack.push_back(make_pair(t, -1));
    while (!dstack.empty()) {
        pair<int, int> curPair = dstack.back();
        dstack.pop_back();
        int cur = curPair.first;
        int parent = curPair.second;
        for (size_t i = 0; i < graph[cur].size(); i++) {
            int nv = graph[cur][i].first;
            ll w = graph[cur][i].second;
            if (nv == parent)
                continue;
            if (dist_t[nv] == -1) {
                dist_t[nv] = dist_t[cur] + w;
                dstack.push_back(make_pair(nv, cur));
            }
        }
    }
}

inline bool in_subtree(int u, int x, const vector<int>& tin, const vector<int>& tout) {
    return (tin[x] <= tin[u] && tin[u] < tout[x]);
}

inline bool same_component(int u, int v, int child, const vector<int>& tin, const vector<int>& tout) {
    return in_subtree(u, child, tin, tout) == in_subtree(v, child, tin, tout);
}
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s, t;
    cin >> n >> s >> t;
    s--; t--;

    vector<vector<pair<int, ll>>> graph(n);
    for (int i = 0; i < n - 1; i++){
        int u, v;
        ll w;
        cin >> u >> v >> w;
        u--; v--;
        graph[u].push_back(make_pair(v, w));
        graph[v].push_back(make_pair(u, w));
    }

    vector<ll> dist_s(n, 0);
    vector<int> par(n, -1), tin(n, 0), tout(n, 0);
    dfs_tree(graph, s, dist_s, par, tin, tout);

    vector<ll> dist_t(n, -1);
    dist_t[t] = 0;
    compute_dist_t(graph, t, dist_t);

    int q;
    cin >> q;
    const ll INF = 1LL << 61;

    for (int i = 0; i < q; i++){
        int a1, b1, a2, b2;
        ll c;
        cin >> a1 >> b1 >> a2 >> b2 >> c;
        a1--; b1--; a2--; b2--;

        int child;
        if (par[a1] == b1)
            child = a1;
        else if (par[b1] == a1)
            child = b1;
        else
            child = a1;
 
        ll ans = INF;

        if (same_component(s, t, child, tin, tout))
            ans = min(ans, dist_s[t]);

        if (same_component(s, a2, child, tin, tout) && same_component(b2, t, child, tin, tout)) {
            ll candidate = dist_s[a2] + c + dist_t[b2];
            ans = min(ans, candidate);
        }

        if (same_component(s, b2, child, tin, tout) && same_component(a2, t, child, tin, tout)) {
            ll candidate = dist_s[b2] + c + dist_t[a2];
            ans = min(ans, candidate);
        }
 
        cout << (ans < INF ? ans : -1) << "\n";
    }
 
    return 0;
}
