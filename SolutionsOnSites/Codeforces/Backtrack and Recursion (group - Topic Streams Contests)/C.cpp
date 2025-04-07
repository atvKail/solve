#include <iostream>
#include <vector>
#include <queue>
using namespace std;
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;
    vector<string> cave(n);
    for (int i = 0; i < n; i++){
        cin >> cave[i];
    }
    
    int r1, c1, r2, c2;
    cin >> r1 >> c1 >> r2 >> c2;
    r1--; c1--; r2--; c2--;
    
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    queue<pair<int, int>> q;
    q.push(make_pair(r1, c1));
    visited[r1][c1] = true;
    
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    
    while(!q.empty()){
        pair<int, int> cur = q.front();
        q.pop();
        int x = cur.first, y = cur.second;
        for(int d = 0; d < 4; d++){
            int nx = x + dx[d], ny = y + dy[d];

            if(nx < 0 || ny < 0 || nx >= n || ny >= m) {
                continue;
            }

            if(visited[nx][ny]) {
                continue;
            }

            if(nx == r2 && ny == c2){
                visited[nx][ny] = true;
                q.push(make_pair(nx, ny));
            } else if(cave[nx][ny]=='.'){
                visited[nx][ny] = true;
                q.push(make_pair(nx, ny));
            }
        }
    }
    
    if(!visited[r2][c2]){
        cout << "NO";
        return 0;
    }
    
    int cnt = 0;
    for (int d = 0; d < 4; d++){
        int nx = r2 + dx[d], ny = c2 + dy[d];
        if(nx < 0 || ny < 0 || nx >= n || ny >= m) {
            continue;
        }
        if(visited[nx][ny]) {
            cnt++;
        }
    }
    
    if(r1 == r2 && c1 == c2) {
        cout << (cnt >= 1 ? "YES" : "NO");
    } else {
        if(cave[r2][c2]=='X') {
            cout << (cnt >= 1 ? "YES" : "NO");
        } else {
            cout << (cnt >= 2 ? "YES" : "NO");
        }
    }
    return 0;
}
