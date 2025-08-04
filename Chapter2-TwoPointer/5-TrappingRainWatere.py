"""
You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1

Return the maximum area of water that can be trapped between between the bars
"""


class Solution:

  def trap(self, height: list[int]) -> int:
    n = len(height)
    if n == 0:
      return 0

    leftMax = [0] * n
    rightMax = [0] * n

    leftMax[0] = height[0]
    for i in range(1, n):
      leftMax[i] = max(leftMax[i - 1], height[i])

    rightMax[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
      rightMax[i] = max(rightMax[i + 1], height[i])

    res = 0
    for i in range(n):
      res += min(leftMax[i], rightMax[i]) - height[i]
    return res


if __name__ == "__main__":
  TestCase = Solution()

  height1 = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
  result1 = TestCase.trap(height1)
  print(result1)
"""
这个题实际上就是之前那个接雨水的多了一个高度的问题.但是可以通过左右max 来解决, 然后min(left, right) - 当前高度, 如果大于0, 则总数上++

maxLeft 是一个array, 这个array当前index = 之前index的最大值
maxRight 是一个array, 这个array当前index = 后面index的最大值
input是高度array

input     | 0 1 0 2 1 0 1 3 2 1 2 1
------------------------------------
maxLeft   | 0 0 1 1 2 2 2 2 3 3 3 3
------------------------------------
maxRight  | 3 3 3 3 3 3 3 2 2 2 1 0
------------------------------------
min(L, R) | 0 0 1 1 2 2 2 2 2 2 1 0
------------------------------------
min(L, R) - h[i] >= 0, then ++
"""


