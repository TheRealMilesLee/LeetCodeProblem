"""
Design a stack class that supports the push, pop, top, and getMin operations.

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

Each function should run in O(1)O(1) time.
"""


class MinStack:

  def __init__(self):
    self.stack = []

  def push(self, val: int) -> None:
    self.stack.append(val)

  def pop(self) -> None:
    self.stack.pop()

  def top(self) -> int:
    return self.stack[len(self.stack) - 1]

  def getMin(self) -> int:
    minVal = float("inf")

    for index in self.stack:
      if index < minVal:
        minVal = index

    return minVal


if __name__ == "__main__":
  minStack = MinStack()
  minStack.push(1)
  minStack.push(2)
  minStack.push(0)
  checkpoint = minStack.getMin()
  minStack.pop()
  checkpoint2 = minStack.top()
  checkpoint3 = minStack.getMin()

  print(checkpoint)
  print(checkpoint2)
  print(checkpoint3)
"""
简单题简单做, 用list来模拟一个倒过来的stack就好, 主要就是记住语法, append是往后面加入, pop是把最后一位弹出来
"""
