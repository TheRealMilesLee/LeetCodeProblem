"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.
"""


class Solution:

  def longestConsecutive(self, nums: list[int]) -> int:
    if not nums:
      return 0
    res = 0
    nums.sort()

    curr = nums[0]
    streak = 0
    i = 0

    while i < len(nums):
      if curr != nums[i]:
        curr = nums[i]
        streak = 0
      while i < len(nums) and nums[i] == curr:
        i += 1
      streak += 1
      curr += 1
      res = max(res, streak)
    return res


if __name__ == "__main__":
  TestCase = Solution()

  nums1 = [2, 20, 4, 10, 3, 4, 5]
  Result1 = TestCase.longestConsecutive(nums1)
  print(Result1)

  nums2 = [1, 4, 5, 6, 7, 9, 100, 2, 3, 6, 8]
  Result2 = TestCase.longestConsecutive(nums2)
  print(Result2)
