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

const int MAXN = 200000 + 5;

struct LCT{
    struct Node{
        Node *p = nullptr, *c[2] ={nullptr,nullptr};
        bool rev = false;
        int sz = 1;
    } *T[MAXN];

    LCT(int n){ forn(i,1,n+1) T[i] = new Node(); }

    bool is_root(Node *x){
        return !x->p || (x->p->c[0] != x && x->p->c[1] != x);
    }

    void push(Node *x){
        if(x->rev){
            swap(x->c[0], x->c[1]);
            if(x->c[0]) x->c[0]->rev ^= 1;
            if(x->c[1]) x->c[1]->rev ^= 1;
            x->rev = false;
        }
    }

    void pull(Node *x){
        x->sz = 1;
        if(x->c[0]) x->sz += x->c[0]->sz;
        if(x->c[1]) x->sz += x->c[1]->sz;
    }

    void rotate(Node *x){
        Node *p = x->p, *g = p->p;
        push(p); push(x);
        bool r = x == p->c[1];
        Node *b = x->c[!r];
        if(!is_root(p)) g->c[p == g->c[1]] = x;
        x->p = g;
        x->c[!r] = p;
        p->p = x;
        p->c[r] = b;
        if(b) b->p = p;
        pull(p);
        pull(x);
    }

    void splay(Node *x){
        static vector<Node*> stk;
        stk.clear();
        for(Node *u = x; ; u = u->p){
            stk.pb(u);
            if(is_root(u)) break;
        }
        for(auto it = stk.rbegin(); it != stk.rend(); ++it) push(*it);
        while(!is_root(x)){
            Node *p = x->p, *g = p->p;
            if(!is_root(p))
                rotate((x == p->c[1]) == (p == g->c[1]) ? p : x);
            rotate(x);
        }
    }

    void access(Node *x){
        Node *last = nullptr;
        for(Node *u = x; u; u = u->p){
            splay(u);
            u->c[1] = last;
            pull(u);
            last = u;
        }
        splay(x);
    }

    void make_root(Node *x){
        access(x);
        x->rev ^= 1;
    }

    Node* find_root(Node *x){
        access(x);
        while(true){
            push(x);
            if(!x->c[0]) break;
            x = x->c[0];
        }
        splay(x);
        return x;
    }

    void link(int u, int v){
        Node *x = T[u], *y = T[v];
        make_root(x);
        if(find_root(y) != x) x->p = y;
    }

    void cut(int u, int v){
        Node *x = T[u], *y = T[v];
        make_root(x);
        access(y);
        if(y->c[0]==x && !x->c[1]){
            y->c[0]=nullptr;
            x->p=nullptr;
            pull(y);
        }
    }

    int path_size(int u, int v){
        Node *x = T[u], *y = T[v];
        make_root(x);
        access(y);
        return y->sz;
    }

    bool connected(int u, int v){
        return find_root(T[u]) == find_root(T[v]);
    }
};

int g[MAXN];
bool drop_edge[MAXN];
int cyc_sz[MAXN];
ll S = 0;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if(!(cin >> n >> q)) return 0;
    forn(i, 1, n + 1) cin >> g[i];

    vi vis(n + 1);
    forn(i, 1, n + 1){
        if(!vis[i]){
            int u = i;
            vi stk;
            while(!vis[u]){
                vis[u] = i;
                stk.pb(u);
                u = g[u];
            }
            if(vis[u] == i){
                vi cyc;
                int v;
                do{
                    v = stk.back();
                    stk.pop_back();
                    cyc.pb(v);
                } while(v != u);
                int x = cyc[0];
                drop_edge[x] = 1;
                cyc_sz[x] = cyc.size();
                S += cyc_sz[x] - 1;
            }
        }
    }

    LCT lct(n);
    forn(i, 1, n + 1)
        if(!drop_edge[i]) lct.link(i, g[i]);

    while(q--){
        int x, y;
        ll k;
        cin >> x >> y >> k;
        int old = g[x];
        if(drop_edge[x]){
            S -= cyc_sz[x] - 1;
            drop_edge[x] = 0;
        } else lct.cut(x, old);
        g[x] = y;
        if(!lct.connected(x, y)){
            lct.link(x, y);
        } else{
            int r = lct.path_size(y, x);
            drop_edge[x] = 1;
            cyc_sz[x] = r;
            S += r - 1;
        }
        ll E = n - S;
        int km = k % 3, res;
        if(km == 0) res = E > 0 ? 0 : 1;
        else if(km == 1) res = 1;
        else res = (E & 1) ? 2 : 1;
        cout << res << "\n";
    }
    return 0;
}
