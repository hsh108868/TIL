#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main() {

    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    int n;
    cin >> n;
    queue<int> q;
    string queueString;

    for(int i = 0; i < n; i++) {
        cin >> queueString;
        if(queueString == "push") {
            int m;
            cin >> m;
            q.push(m);
        } else if (queueString == "pop") {
            if(q.empty()) {
                cout << -1 << "\n";
            } else{
                cout << q.front() << "\n";
                q.pop();
            }
        } else if (queueString == "size") {
            cout << q.size() << "\n";
        } else if (queueString == "empty") {
            if(q.empty()) {
                cout << 1 << "\n";
            } else {
                cout << 0 << "\n";
            }
        } else if (queueString == "front") {
            if(q.empty()) {
                cout << -1 << "\n";
            } else {
                cout << q.front() << "\n";
            }
        } else if (queueString == "back") {
            if(q.empty()) {
                cout << -1 << "\n";
            } else {
                cout << q.back() << "\n";
            }
        }
    }
    return 0;
} 