#include <iostream>
#include <vector>
#include <unordered_set>
#include <array>
#include <algorithm>
#include <cmath>
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

struct Frac{
    long long num, den;

    Frac(long long n = 0, long long d = 1){
        if(d < 0){
            n = -n;
            d = -d;
        }
        long long g = __gcd(abs(n), abs(d));
        num = n / g;
        den = d / g;
        if(den == 0){
            num = 1;
            den = 0;
        }
    }

    bool operator==(const Frac& o) const{
        return num == o.num && den == o.den;
    }

    Frac operator+(const Frac& o) const{
        return Frac(num * o.den + o.num * den, den * o.den);
    }

    Frac operator-(const Frac& o) const{
        return Frac(num * o.den - o.num * den, den * o.den);
    }

    Frac operator*(const Frac& o) const{
        return Frac(num * o.num, den * o.den);
    }

    Frac divInt(long long v) const{
        return Frac(num, den * v);
    }

    bool operator<(const Frac& o) const{
        if(den == 0 && o.den == 0) return false;
        if(den == 0) return false;
        if(o.den == 0) return true;
        return num * o.den < o.num * den;
    }
};

struct State{
    Frac x, y;
    int vx, vy;

    bool operator==(const State& o) const{
        return x == o.x && y == o.y && vx == o.vx && vy == o.vy;
    }
};

struct StateHash{
    size_t operator()(const State& s) const{
        size_t h = hash<long long>()(s.x.num);
        h ^= hash<long long>()(s.x.den) + 0x9e3779b9 + (h << 6) + (h >> 2);
        h ^= hash<long long>()(s.y.num) + 0x9e3779b9 + (h << 6) + (h >> 2);
        h ^= hash<int>()(s.vx) + 0x9e3779b9 + (h << 6) + (h >> 2);
        h ^= hash<int>()(s.vy) + 0x9e3779b9 + (h << 6) + (h >> 2);
        return h;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--){
        long long n, x, y, vx, vy;
        cin >> n >> x >> y >> vx >> vy;

        Frac xi(x), yi(y);
        Frac n_frac(n);

        unordered_set<State, StateHash> seen;
        int cnt = 0;
        bool escaped = false;
        State current{xi, yi, static_cast<int>(vx), static_cast<int>(vy)};
        const int MAX_ITER = 1e6;
        int iter = 0;

        while (iter++ < MAX_ITER){
            if((current.x == Frac(0) && current.y == Frac(0)) ||
                (current.x == Frac(0) && current.y == n_frac) ||
                (current.x == n_frac && current.y == Frac(0))){
                escaped = true;
                break;
            }

            if(seen.find(current) != seen.end()){
                break;
            }
            seen.insert(current);

            Frac t1 = (current.vy < 0) ? current.y.divInt(-current.vy) : Frac(1, 0);
            Frac t2 = (current.vx < 0) ? current.x.divInt(-current.vx) : Frac(1, 0);
            Frac t3 = (current.vx + current.vy > 0) ? (n_frac - current.x - current.y).divInt(current.vx + current.vy) : Frac(1, 0);

            Frac t = min({t1, t2, t3});
            if(t.den == 0 || t.num <= 0){
                current.x = current.x + Frac(current.vx) * t;
                current.y = current.y + Frac(current.vy) * t;
                continue;
            }

            Frac x_new = current.x + Frac(current.vx) * t;
            Frac y_new = current.y + Frac(current.vy) * t;

            if(x_new == Frac(0) && y_new == Frac(0)){
                escaped = true;
                break;
            }
            if(x_new == Frac(0) && y_new == n_frac){
                escaped = true;
                break;
            }
            if(x_new == n_frac && y_new == Frac(0)){
                escaped = true;
                break;
            }

            int new_vx = current.vx, new_vy = current.vy;
            if(t == t1){
                new_vy = -new_vy;
            } else if(t == t2){
                new_vx = -new_vx;
            } else{
                int temp = new_vx;
                new_vx = -new_vy;
                new_vy = -temp;
            }

            current ={x_new, y_new, new_vx, new_vy};
            cnt++;
        }

        if(escaped){
            cout << cnt << "\n";
        } else{
            cout << -1 << "\n";
        }
    }

    return 0;
}

// tl 5