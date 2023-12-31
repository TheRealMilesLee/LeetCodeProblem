/*
 * @lc app=leetcode.cn id=13 lang=cpp
 *
 * [13] 罗马数字转整数
 */

#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;
// @lc code=start
class Solution
{
private:
  unordered_map<char, int> symbolValues = {
      {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000},
  };

public:
  int romanToInt(string s)
  {
    int ans = 0;
    for (size_t loop = 0; loop < s.length(); loop++)
    {
      int value = symbolValues[s[loop]];
      if (loop < s.length() - 1 && value < symbolValues[s[loop + 1]])
      {
        ans -= value;
      }
      else
      {
        ans += value;
      }
    }
    return ans;
  }
};
// @lc code=end
