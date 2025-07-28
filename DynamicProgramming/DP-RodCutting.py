"""
Given a rod length n, each length of rod i has correspond price[i]. You can cut whatever you like, but we need the maximum profit

e.g.
If the length = 4, price = [0,1,5,8,9], it could be cut as
- price[4] = 9
- price[1] + price[3] = 1 + 8 = 9
- price[2] + price[2] = 5 + 5 = 10 // Maximum

So the maximum profit is 10
"""

class Solution:
  def rodCutting(self, price, n):
    # initialization
    dp = [0] * (n+1)

    for i in range(1, n+1):
      max_val = 0
      for j in range(1, i+1):
        max_val = max(max_val, price[j] + dp[i - j])
      dp[i] = max_val
    return dp[n]

if __name__ == "__main__":
  TestCase = Solution()

  price1 = [0,1,5,8,9]
  results1 = TestCase.rodCutting(price1, 4)
  print(results1)

