"""
Given an array of integers temperatures where temperatures[i] represents the
daily temperatures on the ith day

Return an array result where result[i] is the number of days after the ith day
before a warmer temperature appears on a future day. If there is no day in the
future where a warmer temperature will appear for the ith day, set result[i]
to 0 instead
"""


class Solution:

  def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures)
    stack = []  # pair: [temp, index]

    for i, t in enumerate(temperatures):
      while stack and t > stack[-1][0]:
        stackT, stackInd = stack.pop()
        res[stackInd] = i - stackInd
      stack.append((t, i))
    return res


if __name__ == "__main__":
  TestCase = Solution()

  temperatures = [30, 38, 30, 36, 35, 40, 28]
  results = TestCase.dailyTemperatures(temperatures)
  print(results)
"""
stack存的是还没有等到更高温度的日子, 是一个tuple, 左边是当前温度, 右边是当前温度所在的index

指针向前走,如果看到了比当前温度更高的, 就弹出当前的温度, 并且把计数写入array, 然后将新的最高压入stack
"""
