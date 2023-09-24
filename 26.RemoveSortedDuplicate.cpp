/*
 * @lc app=leetcode.cn id=26 lang=cpp
 *
 * [26] 删除有序数组中的重复项
 */

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// @lc code=start
class Solution
{
public:
  int removeDuplicates(vector<int>& nums)
  {
      vector<int> tempVect;
      sort(nums.begin(), nums.end());
      tempVect.push_back(nums.at(0));
      for (size_t loop = 1; loop < nums.size(); loop++)
      {
        if (nums.at(loop - 1) == nums.at(loop))
        {
            continue;
        }
        else
        {
            tempVect.push_back(nums.at(loop));
        }
      }
      nums.clear();
      for (int CopyBack : tempVect)
      {
          nums.push_back(CopyBack);
      }
      return nums.size();
  }
};
// @lc code=end
