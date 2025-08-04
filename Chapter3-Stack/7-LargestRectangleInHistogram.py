"""
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.
"""


class Solution:

  def largestRectangleArea(self, heights: list[int]) -> int:
    n = len(heights)
    stack = []

    leftMost = [-1] * n
    for i in range(n):
      while stack and heights[stack[-1]] >= heights[i]:
        stack.pop()
      if stack:
        leftMost[i] = stack[-1]
      stack.append(i)

    stack = []
    rightMost = [n] * n
    for i in range(n - 1, -1, -1):
      while stack and heights[stack[-1]] >= heights[i]:
        stack.pop()
      if stack:
        rightMost[i] = stack[-1]
      stack.append(i)

    maxArea = 0
    for i in range(n):
      leftMost[i] += 1
      rightMost[i] -= 1
      maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))
    return maxArea


if __name__ == "__main__":
  TestCase = Solution()

  heights = [7, 1, 7, 2, 2, 4]
  result1 = TestCase.largestRectangleArea(heights)
  print(result1)
