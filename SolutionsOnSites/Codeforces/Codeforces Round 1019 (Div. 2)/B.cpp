#include <iostream>
#include <vector>
using namespace std;

#define forn(i, l, r) for (int i = l; i < r; ++i)
#define all(a) a.begin(), a.end()
#define f first
#define s second
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--){
        int n;
        cin >> n;
        string s;
        cin >> s;

        int moves = (s[0] == '1');
        forn(i, 1, n){
            if(s[i] != s[i - 1]) moves++;
        }
        int M = n + moves;

        vector<int> pos01, pos10;
        forn(i, 0, n - 1){
            if(s[i] == '0' && s[i + 1] == '1') pos01.push_back(i);
            if(s[i] == '1' && s[i + 1] == '0') pos10.push_back(i);
        }

        int dlt = 0;
        if((int)pos01.size() >= 2 && pos01.back() - pos01.front() >= 2){
            dlt = 2;
        } else if((int)pos10.size() >= 2 && pos10.back() - pos10.front() >= 2){
            dlt = 2;
        } else{
            bool found101 = false;
            forn(i, 1, n - 1){
                if(s[i - 1] == '1' && s[i] == '0' && s[i + 1] == '1'){
                    found101 = true;
                    break;
                }
            }
            if(found101){
                dlt = 2;
            } else{
                
                int total_trans = (s[0] == '1');
                forn(i, 1, n){
                    if(s[i] != s[i - 1]) total_trans++;
                }
                if(s[0] == '1' && s[n-1] == '1' && total_trans >= 2){
                    dlt = 2;
                }
            }
        }

        if(dlt == 0){
            bool one = false;
            if(s[0] == '1' && s[n - 1] == '0'){
                one = true;
            }
            if(!one){
                forn(i, 0, n - 1){
                    if(s[i] != s[i + 1] && s[n - 1] == s[i]){
                        one = true;
                        break;
                    }
                }
            }
            if(!one){
                forn(i, 0, n - 1){
                    if(s[i] != s[i + 1] && s[0] == s[i + 1]){
                        one = true;
                        break;
                    }
                }
            }
            if(one) dlt = 1;
        }
        cout << (M - dlt) << "\n";
    }
}