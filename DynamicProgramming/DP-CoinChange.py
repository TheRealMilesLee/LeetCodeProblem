"""
Given a set of coins = [1,2,5] and a target price amount = 11, calculate the minimum number of coins that could add up to this number

e.g.
Input: coins = [1,2,5], amount = 11
Output: 3
Because 11 = 5 + 5 + 1
"""


class Solution:

  def coinChange(self, coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
      for coin in coins:
        if i - coin >= 0:
          dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
  TestCase = Solution()

  coins1 = [1, 2, 5]
  amount = 11
  Results1 = TestCase.coinChange(coins1, amount)
  print(Results1)
