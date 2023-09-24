/*
 * @lc app=leetcode.cn id=88 lang=cpp
 *
 * [88] 合并两个有序数组
 * Jump to m position, start merge
 */
#include <algorithm>
#include <iostream>
#include <vector>


using namespace std;
// @lc code=start
class Solution
{
public:
  void merge(vector<int>& nums1, int m, vector<int>& nums2, int n)
  {
    size_t appendIndex = 0;
    for (size_t loop = 0; loop < nums1.size(); loop++)
    {
      if (loop >= m)
      {
        nums1.at(loop) = nums2.at(appendIndex);
        appendIndex++;
      }
    }
    sort(nums1.begin(), nums1.end());
  }
};

// @lc code=end
