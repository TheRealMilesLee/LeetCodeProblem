/*
 * @lc app=leetcode.cn id=169 lang=cpp
 *
 * [169] 多数元素
 */
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;
// @lc code=start
class Solution
{
public:
  int majorityElement(vector<int>& nums)
  {
    map<int, int> CountMap;
    for (size_t loop = 0; loop < nums.size(); loop++)
    {
      if (CountMap.end() != CountMap.find(nums.at(loop)))
      {
        CountMap.at(nums.at(loop))++;
      }
      else
      {
        CountMap.insert(pair<int, int>(nums.at(loop), 1));
      }
    }
    for (auto count : CountMap)
    {
      if (nums.size() / 2 < count.second)
      {
        return count.first;
      }
    }
    cout << 3 / 2;
    return 0;
  }
};
// @lc code=end
