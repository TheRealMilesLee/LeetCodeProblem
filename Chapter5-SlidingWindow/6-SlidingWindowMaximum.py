"""
You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.
"""

from collections import deque


class Solution:

  def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
    output = []
    q = deque()  # index
    l = r = 0

    while r < len(nums):
      while q and nums[q[-1]] < nums[r]:
        q.pop()
      q.append(r)

      if l > q[0]:
        q.popleft()

      if (r + 1) >= k:
        output.append(nums[q[0]])
        l += 1
      r += 1

    return output


if __name__ == '__main__':
  TestCase = Solution()
  nums = [1, 2, 1, 0, 4, 2, 6]
  Result1 = TestCase.maxSlidingWindow(nums, 3)
  print(Result1)
