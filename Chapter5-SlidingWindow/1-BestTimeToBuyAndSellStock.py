"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
"""


class Solution:

  def maxProfit(self, prices: list[int]) -> int:
    left = 0
    right = 1

    maxProfit = 0

    while right < len(prices):
      if prices[left] < prices[right]:
        currentProfit = prices[right] - prices[left]
        maxProfit = max(maxProfit, currentProfit)
      else:
        left = right
      right += 1
    return maxProfit


if __name__ == '__main__':
  TestCase = Solution()
  prices = [7, 1, 5, 3, 6, 4]
  Result1 = TestCase.maxProfit(prices)
  print(Result1)

  prices2 = [7, 6, 4, 3, 1]
  Result2 = TestCase.maxProfit(prices2)
  print(Result2)
"""
实现方式还是用双指针, 一个左一个右, 左右两个指针是挨着的, 然后就看右边的price是否比左边的高, 如果左边比右边高的话说明高位在左低位在右, 于是就要把左边指针向右边移动
"""
