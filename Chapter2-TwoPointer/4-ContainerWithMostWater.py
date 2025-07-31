"""
Given an integer array heights where heights[i] represents the height of the ith bar

You may choose any two bars to form a container. Return the maximum amount of water a container can store.
"""

class Solution:
  def maxArea(self, heights: list[int]) -> int:
    left = 0
    right = len(heights) - 1
    results = 0

    while left < right:
      currentArea = min(heights[left], heights[right]) * (right - left) # Length * height, the area was determined by the shorter one
      results = max(results, currentArea)

      if heights[left] <= heights[right]:
        left += 1
      else:
        right += 1
    return results

if __name__ == "__main__":
  TestCase = Solution()

  height = [1,7,2,5,4,7,3,6]
  results1 = TestCase.maxArea(height)
  print(results1)

  
