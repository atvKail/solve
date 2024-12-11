#include <iostream>
#include <string>
#include <sstream>

using namespace std;

class Account {
public:
    double balance = 0.0;
    double cashback = 0.0;
};

void solve(Account& account, const string& command) {
    stringstream ss(command);
    string cmd;
    double amount;
    ss >> cmd >> amount;
    if (cmd == "replenishment") {
        account.balance += amount;
    } 
    else if (cmd == "transaction") {
        if (account.balance >= amount) { // комиссия
            double commission = amount * 0.02; // 2% от суммы транзакции
            double cashback = commission * 0.5; // 1% из 2% на кэшбэк
            account.balance -= amount;
            account.cashback += cashback;
        }
    }
}

int main() {
    Account account;
    string command;

    while (true) {
        getline(cin, command);
        for (auto & c: command) c = tolower(c);

        if (command == "end") {
            cout << "balance: " << account.balance << ", cashback: " << account.cashback << endl;
            break;
        }

        solve(account, command);

        if (command == "get") {
            cout << "balance: " << account.balance << ", cashback: " << account.cashback << endl;
        }
    }

    return 0;
}                    // task 31




#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Transaction {
public:
    int clientId;
    double x, y;

    Transaction(int clientId, double x, double y) : clientId(clientId), x(x), y(y) {}
};

vector<int> solve(int n, int m, const vector<Transaction>& transactions, double pointSaleX, double pointSaleY) {
    unordered_map<int, int> clientTransactions;

    for (const auto& transaction : transactions) {
        double distance = sqrt(pow(transaction.x - pointSaleX, 2) + pow(transaction.y - pointSaleY, 2));
        if (distance <= 700) {
            clientTransactions[transaction.clientId]++;
        }
    }

    vector<int> result;
    for (const auto& pair : clientTransactions) {
        if (pair.second >= 2) {
            result.push_back(pair.first);
        }
    }

    sort(result.begin(), result.end());

    return result;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<Transaction> transactions;
    for (int i = 0; i < m; ++i) {
        int clientId;
        double x, y;
        cin >> clientId >> x >> y;
        transactions.push_back(Transaction(clientId, x, y));
    }

    double pointSaleX, pointSaleY;
    cin >> pointSaleX >> pointSaleY;

    vector<int> result = solve(n, m, transactions, pointSaleX, pointSaleY);

    if (result.empty()) {
        cout << "-1" << endl;
    } else {
        for (size_t i = 0; i < result.size(); ++i) {
            cout << result[i];
            if (i != result.size() - 1) {
                cout << " ";
            }
        }
        cout << endl;
    }

    return 0;
}                // task 33
