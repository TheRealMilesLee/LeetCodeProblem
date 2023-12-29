/*
 * @lc app=leetcode.cn id=2554 lang=cpp
 *
 * [2554] 从一个范围内选择最多整数 I
 */

#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;
// @lc code=start
class Solution
{
public:
  int maxCount(vector<int>& banned, int n, int maxSum)
  {
    unordered_set<int> seen;
    for (auto num : banned)
      seen.insert(num);
    int cnt = 0;
    int sum = 0;
    for (int i = 1; i <= n; i++)
    {
      if (seen.count(i))
      {
        continue;
      }
      sum += i;
      if (sum > maxSum)
      {
        break;
      }
      else
      {
        cnt++;
      }
    }
    return cnt;
  }
};
// @lc code=end
