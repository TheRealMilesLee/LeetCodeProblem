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

    for index in tokens:
      if index == "+":
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
      elif index == "-":
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
      elif index == "*":
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
      elif index == "/":
        a = stack.pop()
        b = stack.pop()
        stack.append(int(b / a))
      else:
        stack.append(int(index))
    return stack[0]
