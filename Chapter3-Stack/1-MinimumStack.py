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
    self.newStack = []

  def push(self, val: int) -> None:
    self.newStack.append(val)

  def pop(self) -> None:
    self.newStack.pop()

  def top(self) -> int:
    return self.newStack[-1]

  def getMin(self) -> int:
    minValue = float('inf')
    for index in self.newStack:
      if index < minValue:
        minValue = index
    return minValue


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
