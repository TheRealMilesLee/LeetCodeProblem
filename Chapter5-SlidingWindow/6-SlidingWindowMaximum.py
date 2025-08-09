"""
You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.
"""
from collections import deque


class Solution:

  def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
    q = deque()  # 存索引, 保证nums[q]递减
    res = []

    for i, num in enumerate(nums):
      # 弹出所有比当前num小的元素索引, 保证q单调递减
      while q and nums[q[-1]] < num:
        q.pop()

      q.append(i)

      # 窗口左边界已经过期的索引弹出
      if q[0] <= i - k:
        q.popleft()

      # 从窗口形成开始，收集结果
      if i >= k - 1:
        res.append(nums[q[0]])

    return res


if __name__ == '__main__':
  TestCase = Solution()
  nums = [1, 2, 1, 0, 4, 2, 6]
  Result1 = TestCase.maxSlidingWindow(nums, 3)
  print(Result1)
