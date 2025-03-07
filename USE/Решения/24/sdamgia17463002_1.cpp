#include <bits/stdc++.h>

using namespace std;

int main() {
    ifstream in("USE/24/sdamgia17463002/24.txt");
    string line;

    if (!in.is_open()) {
        cerr << "Error opening file!" << endl;
        return -1;
    }

    int maxLength = 0;
    bool f = false;

    while (getline(in, line)) {
        int n = line.size();
        int left = 0, right = 0, oCount = 0;
        while (right < n) {
            if (line[left] == 'D' && oCount <= 2){
                maxLength = max(maxLength, right - left + 1);
                f = true;
            }
            if (line[right] != 'D' || f || right == left){
                oCount += (line[right] == 'O') ? 1 : 0;
                f = false;
                right++;
            }
            else{
                oCount += (line[left] == 'O') ? -1 : 0;
                left++;
            }
        }
    }
    cout << maxLength << endl;
    return 0;
}
