/*
 * @lc app=leetcode.cn id=121 lang=cpp
 *
 * [121] 买卖股票的最佳时机
 */
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
// @lc code=start
class Solution
{
public:
  int maxProfit(vector<int>& prices)
  {
    int minprice = 1e9;
    int maxprofit = 0;
    for (int price : prices)
    {
      maxprofit = max(maxprofit, price - minprice);
      minprice = min(price, minprice);
    }
    return maxprofit;
  }
};
// @lc code=end
