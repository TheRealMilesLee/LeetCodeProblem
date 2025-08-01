"""
Given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.
"""


class Solution:

  def generateParenthesis(self, n: int) -> list[str]:
    res = []

    def valid(s: str):
      open = 0
      for c in s:
        open += 1 if c == '(' else -1
        if open < 0:
          return False
      return not open

    def dfs(s: str):
      if n * 2 == len(s):
        if valid(s):
          res.append(s)
        return

      dfs(s + '(')
      dfs(s + ')')

    dfs("")
    return res


if __name__ == "__main__":
  TestCase = Solution()

  result1 = TestCase.generateParenthesis(1)
  print(result1)

  result2 = TestCase.generateParenthesis(3)
  print(result2)
