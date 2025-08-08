"""
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

    position[i] is the position of the ith car (in miles)
    speed[i] is the speed of the ith car (in miles per hour)

The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.
"""


class Solution:

  def carFleet(self, target: int, position: list[int],
               speed: list[int]) -> int:
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)
    stack = []
    for p, s in pair:  # Reverse Sorted Order
      stack.append((target - p) / s)
      if len(stack) >= 2 and stack[-1] <= stack[-2]:
        stack.pop()
    return len(stack)


if __name__ == "__main__":
  TestCase = Solution()

  result1 = TestCase.carFleet(10, [1, 4], [3, 2])
  print(result1)

  result2 = TestCase.carFleet(10, [4, 1, 0, 7], [2, 2, 1, 1])
  print(result2)

"""
用栈来记录当前车队能到达的时间, 如果当前车的时间小于当前栈顶的时间, 说明能追上, 那么不对栈进行操作, 如果大于当前栈顶的时间, 说明追不上前车, 那么就把新的时间压入栈

最后返回栈的长度, 也就是车队的数量
"""
