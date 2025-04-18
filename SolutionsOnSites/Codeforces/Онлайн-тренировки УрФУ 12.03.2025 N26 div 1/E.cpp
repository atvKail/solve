#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

#define forn(i, a, b) for (int i = a; i < b; i++)
#define all(a) a.begin(), a.end()
using ll = long long;

struct Order {
    int p;
    int v;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, s;
    cin >> n >> s;
    map<int, int> bOrders, sOrders;
    
    forn (i, 0, n) {
        char type;
        int p, v;
        cin >> type >> p >> v;
        
        if(type == 'B') bOrders[p] += v;
        else sOrders[p] += v;
    }
    
    vector<Order> sells;
    for (auto &p : sOrders) {
        sells.push_back({p.first, p.second});
    }
    if (sells.size() > (unsigned)s) sells.resize(s);

    sort(sells.begin(), sells.end(), [](const Order &a, const Order &b){
        return a.p > b.p;
    });
    
    vector<Order> buys;
    for (auto &p : bOrders) {
        buys.push_back({p.first, p.second});
    }
    sort(all(buys), [](const Order &a, const Order &b){
        return a.p > b.p;
    });
    if (buys.size() > (unsigned)s) {
        buys.resize(s);
    }
    
    for (auto &o : sells) {
        cout << "S " << o.p << " " << o.v << "\n";
    }
    for (auto &o : buys) {
        cout << "B " << o.p << " " << o.v << "\n";
    }
    
    return 0;
}
