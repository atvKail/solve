#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<int> heapAll;
        for (int i = 0; i < lists.size(); i++) {
            ListNode* currL = lists[i];
            while (currL != nullptr) {
                heapAll.push_back(currL->val);
                currL = currL->next;
            }
        }

        if (heapAll.empty()) return nullptr;
        
        make_heap(heapAll.begin(), heapAll.end(), greater<int>());
        
        ListNode* dummy = new ListNode(0);
        ListNode* tail = dummy;
        
        while (!heapAll.empty()) {
            pop_heap(heapAll.begin(), heapAll.end(), greater<int>());
            int minVal = heapAll.back();
            heapAll.pop_back();
            tail->next = new ListNode(minVal);
            tail = tail->next;
        }
        
        ListNode* result = dummy->next;
        delete dummy;
        return result;
    }
};

int main(){
    vector<ListNode*> lists;
    ListNode L5(5);
    ListNode L4(4, &L5);
    ListNode L3(3, &L4);
    ListNode L2(2, &L3);
    ListNode L1(1, &L2);
    lists.push_back(&L1);

    Solution sol;
    ListNode *res = sol.mergeKLists(lists);

    while (res != nullptr) {
        cout << res->val << ' ';
        res = res->next;
    }
    return 0;
}
