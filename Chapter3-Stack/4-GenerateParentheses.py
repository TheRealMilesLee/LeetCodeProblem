"""
Given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.
"""


class Solution:

  def generateParenthesis(self, n):
    res = [[] for _ in range(n + 1)]
    res[0] = [""]

    for k in range(n + 1):
      for i in range(k):
        for left in res[i]:
          for right in res[k - i - 1]:
            res[k].append("(" + left + ")" + right)

    return res[-1]


if __name__ == "__main__":
  TestCase = Solution()

  result1 = TestCase.generateParenthesis(1)
  print(result1)

  result2 = TestCase.generateParenthesis(3)
  print(result2)

"""
用dp来做, 初始化为空, 然后构造括号里可能出现的组合, 考虑洋葱一样抱进去的还有左右排列的
"""
