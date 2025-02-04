#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            swap(nums1, nums2);
        }

        int m = nums1.size(), n = nums2.size();
        int total = m + n;
        int half = total / 2;

        int left = 0, right = m;

        while (left <= right) {
            int i = left + (right - left) / 2;
            int j = half - i;

            int nums1Left = (i > 0) ? nums1[i - 1] : INT_MIN;
            int nums1Right = (i < m) ? nums1[i] : INT_MAX;
            int nums2Left = (j > 0) ? nums2[j - 1] : INT_MIN;
            int nums2Right = (j < n) ? nums2[j] : INT_MAX;

            if (nums1Left <= nums2Right && nums2Left <= nums1Right) {
                if (total % 2 == 1) {
                    return min(nums1Right, nums2Right);
                } else {
                    return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2.0;
                }
            } else if (nums1Left > nums2Right) {
                right = i - 1;
            } else {
                left = i + 1;
            }
        }
        return 0.0;
    }
};

int main(){
    Solution sol;
    int m, n;
    cin >> m >> n;
    vector<int> nums1(m, 0), nums2(n, 0);

    for(int i = 0; i < m; i++){
        cin >> nums1[i];
    }

    for(int i = 0; i < n; i++){
        cin >> nums2[i];
    }

    cout << sol.findMedianSortedArrays(nums1, nums2) << endl;
}