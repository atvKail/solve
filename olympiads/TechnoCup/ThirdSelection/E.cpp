// #include <bits/stdc++.h>
// using namespace std;

// vector<bool> sieve(int limit) {
//     vector<bool> is_prime(limit + 1, true);
//     is_prime[0] = is_prime[1] = false;
//     for (int i = 2; i * i <= limit; ++i) {
//         if (is_prime[i]) {
//             for (int j = i * i; j <= limit; j += i) {
//                 is_prime[j] = false;
//             }
//         }
//     }
//     return is_prime;
// }

// int sum_dgts_in_base(int x, int b) {
//     int ttl = 0;
//     while (x > 0) {
//         ttl += x % b;
//         x /= b;
//     }
//     return ttl;
// }

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);
//     cout.tie(nullptr);

//     int t;
//     cin >> t;
//     vector<int> tcases(t);

//     for (int i = 0; i < t; ++i) {
//         cin >> tcases[i];
//     }

//     int maxx = *max_element(tcases.begin(), tcases.end());

//     vector<bool> isPrime = sieve(maxx);

//     for (int x : tcases) {
//         int count = 0;
//         for (int b = 2; b <= x; ++b) {
//             int dgts_sum = sum_dgts_in_base(x, b);
//             int diff = x - dgts_sum;
//             if (diff > 1 && isPrime[diff]) {
//                 ++count;
//             }
//         }
//         cout << count << endl;
//     }

//     return 0;
// }


#include <bits/stdc++.h>
using namespace std;

const int MAX = 100000000;

vector<bool> sieve(int limit) {
    vector<bool> is_prime(limit + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i <= limit; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j <= limit; j += i) {
                is_prime[j] = false;
            }
        }
    }
    return is_prime;
}

int sum_dgts_in_base(int x, int b) {
    int ttl = 0;
    while (x > 0) {
        ttl += x % b;
        x /= b;
    }
    return ttl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    vector<bool> isPrime = sieve(MAX);
    
    int t;
    cin >> t;
    vector<int> tcases(t);

    for (int i = 0; i < t; ++i) {
        cin >> tcases[i];
    }

    for (int x : tcases) {
        int count = 0;
        for (int b = 2; b <= x; ++b) {
            int dgts_sum = sum_dgts_in_base(x, b);
            int diff = x - dgts_sum;
            if (diff > 1 && isPrime[diff]) {
                ++count;
            }
        }
        cout << count << endl;
    }

    return 0;
}                   // На 58 баллов закрыта задача E
