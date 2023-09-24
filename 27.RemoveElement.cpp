/*
 * @lc app=leetcode.cn id=27 lang=cpp
 *
 * [27] 移除元素
 */
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
// @lc code=start
class Solution
{
public:
  int removeElement(vector<int>& nums, int val)
  {
    vector<int> SwapVect;
    for (int Copy : nums)
    {
      if (Copy == val)
      {
        continue;
      }
      else
      {
        SwapVect.push_back(Copy);
      }
    }
    nums.clear();
    for (int PushCopy : SwapVect)
    {
      nums.push_back(PushCopy);
    }
      return nums.size();
    }
};
// @lc code=end
