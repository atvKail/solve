#include <iostream>

using namespace std;

class Solution {
public:
    int v[13] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
    string r[13] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};

    string intToRoman(int n) {
        string ans = "";
        for (int i = 0; n; i++){
            while (n >= v[i]) {
                ans += r[i];
                n -= v[i];
            }
        }
        return ans;
    }
};