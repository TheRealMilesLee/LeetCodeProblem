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

"""
stack代表的是当前我们正在考虑的高度, 如果当前高度不能再向右延展了, 那么就从stack中pop出来

返回的maxArea就是计算的length x height的最大值

对于stack来说, 存的是当前bar的index和height, 如果当前的height比上一个height小, 那么先计算面积以后再pop掉上一个然后放入新的. 面积的计算方法就是上一个的height x 上一个index到当前index的距离, 然后更新到max area里. 如果当前的height比上一个height大, 则只是把当前的height和当前的index继续推入栈里面
"""
