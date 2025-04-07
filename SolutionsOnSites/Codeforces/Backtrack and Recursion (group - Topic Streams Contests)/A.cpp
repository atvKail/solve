#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int n, m;
vector<string> board;
vector<vector<int>> dp;
vector<vector<int>> used;
bool cycle = false;

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

char nextChar(char c) {
    if(c == 'D') return 'I';
    if(c == 'I') return 'M';
    if(c == 'M') return 'A';
    if(c == 'A') return 'D';
    return '#';
}

int dfs(int i, int j) {
    if(used[i][j] == 1) {
        cycle = true;
        return 0;
    }
    if(used[i][j] == 2) {
        return dp[i][j];
    }
    
    used[i][j] = 1;
    int best = (board[i][j] == 'A') ? 1 : 0;
    char nc = nextChar(board[i][j]);
    
    for(int d = 0; d < 4; d++) {
        int ni = i + dx[d], nj = j + dy[d];
        if(ni < 0 || ni >= n || nj < 0 || nj >= m) {
            continue;
        }
        if(board[ni][nj] == nc) {
            int candidate = dfs(ni, nj);
            if(board[i][j] == 'A') {
                candidate += 1;
            }
            best = max(best, candidate);
        }
    }
    used[i][j] = 2;
    dp[i][j] = best;
    return best;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> n >> m;
    board.resize(n);
    for (int i = 0; i < n; i++){
        cin >> board[i];
    }
    dp.assign(n, vector<int>(m, 0));
    used.assign(n, vector<int>(m, 0));

    int ans = 0;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            if (board[i][j] == 'D') {
                int res = dfs(i, j);
                if (cycle) {
                    cout << "Poor Inna!";
                    return 0;
                }
                ans = max(ans, res);
            }
        }
    }
    if (ans == 0) {
        cout << "Poor Dima!";
    } else {
        cout << ans;
    }
    return 0;
}
