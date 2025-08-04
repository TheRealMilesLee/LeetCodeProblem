"""
Given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.
"""


class Solution:

  def generateParenthesis(self, n: int) -> list[str]:
    stack = []
    res = []

    def backtrack(openN, closedN):
      if openN == closedN == n:
        res.append("".join(stack))
        return

      if openN < n:
        stack.append("(")
        backtrack(openN + 1, closedN)
        stack.pop()
      if closedN < openN:
        stack.append(")")
        backtrack(openN, closedN + 1)
        stack.pop()

    backtrack(0, 0)
    return res


if __name__ == "__main__":
  TestCase = Solution()

  result1 = TestCase.generateParenthesis(1)
  print(result1)

  result2 = TestCase.generateParenthesis(3)
  print(result2)
