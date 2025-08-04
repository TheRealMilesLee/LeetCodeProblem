"""
Given an array of strings tokens trhat represents a valid arithmetic expression in reverse polish notation.

Return the integer that represents the evaluation of the expression

    The operands may be integers or the results of other operations.
    The operators include '+', '-', '*', and '/'.
    Assume that division between integers always truncates toward zero.

"""


class Solution:

  def evalRPN(self, tokens: list[str]) -> int:
    stack = []

    operator = ["*", "+", "-", "/"]
    for index in tokens:
      if index not in operator:
        stack.append(int(index))
      else:
        if index == "+":
          a, b = stack.pop(), stack.pop()
          stack.append(a + b)
        elif index == "-":
          a, b = stack.pop(), stack.pop()
          stack.append(b - a)
        elif index == "*":
          a, b = stack.pop(), stack.pop()
          stack.append(a * b)
        else:
          a, b = stack.pop(), stack.pop()
          stack.append(int(b / a))

    return stack[0]


if __name__ == '__main__':
  TestCase = Solution()
  operation = ["2", "1", "+", "3", "*"]
  Result1 = TestCase.evalRPN(operation)
  print(Result1)


"""
三步走思路

1. 用array模拟栈, 走一个循环将数字转int以后存进去
2. 如果遇到符号就pop两个出来进行运算, 注意运算顺序, 因为栈是lifo的所以对于除法和减法要反过来
3. 将运算结果放回去
"""
