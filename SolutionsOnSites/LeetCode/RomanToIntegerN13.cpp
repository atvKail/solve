#include <map>
#include <iostream>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        map<char, int> dict;
        dict['I'] = 1;
        dict['V'] = 5;
        dict['X'] = 10;
        dict['L'] = 50;
        dict['C'] = 100;
        dict['D'] = 500;
        dict['M'] = 1000;

        int n = s.length();
        int Number = dict[s[n - 1]];
        for (int i = n - 2; i >= 0; i--) {
            if (dict[s[i]] >= dict[s[i + 1]]) {
                Number += dict[s[i]];
            }
            else {
                Number -= dict[s[i]];
            }
        }
        cout << Number;
        return Number;  
    }
};