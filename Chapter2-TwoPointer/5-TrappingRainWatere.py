"""
You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1

Return the maximum area of water that can be trapped between between the bars
"""


class Solution:

  def trap(self, height: list[int]) -> int:
    left = 0
    right = len(height) - 1

    leftMax = height[left]
    rightMax = height[right]

    result = 0

    while left < right:
      if leftMax < rightMax:
        left += 1
        leftMax = max(leftMax, height[left])
        result += leftMax - height[left]
      else:
        right -= 1
        rightMax = max(rightMax, height[right])
        result += rightMax - height[right]
    return result


if __name__ == "__main__":
  TestCase = Solution()

  height1 = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
  result1 = TestCase.trap(height1)
  print(result1)
