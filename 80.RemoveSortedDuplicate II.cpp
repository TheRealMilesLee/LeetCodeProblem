/*
 * @lc app=leetcode.cn id=80 lang=cpp
 *
 * [80] 删除有序数组中的重复项 II
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
  int removeDuplicates(vector<int>& nums)
  {
    map<int, int> CountMap;
    CountMap.insert(make_pair(nums.at(0), 1));
    for (size_t loop = 1; loop < nums.size(); loop++)
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
    nums.clear();
    for (const auto& elem : CountMap)
    {
      cout << elem.first << " " << elem.second << endl;
      if (elem.second > 2)
      {
          nums.push_back(elem.first);
          nums.push_back(elem.first);
      }
      else
      {
        if (elem.second == 1)
        {
          nums.push_back(elem.first);
        }
        else
        {
          nums.push_back(elem.first);
          nums.push_back(elem.first);
        }
      }
    }
        return nums.size();
  }
};
// @lc code=end
