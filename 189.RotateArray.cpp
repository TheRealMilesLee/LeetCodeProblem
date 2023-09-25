/*
 * @lc app=leetcode.cn id=189 lang=cpp
 *
 * [189] 轮转数组
 */
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
// @lc code=start
class Solution
{
public:
  void rotate(vector<int>& nums, int k)
  {
    int n = nums.size();
    k %= n; // In case k is greater than the array size

    // Reverse the entire array
    reverse(nums.begin(), nums.end());

    // Reverse the first part of the array (0 to k-1)
    reverse(nums.begin(), nums.begin() + k);

    // Reverse the second part of the array (k to n-1)
    reverse(nums.begin() + k, nums.end());
  }
};

// @lc code=end
