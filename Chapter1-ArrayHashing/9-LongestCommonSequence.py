"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.
"""

import collections


class Solution:

  def longestConsecutive(self, nums: list[int]) -> int:
    mp = collections.defaultdict(int)
    res = 0

    for num in nums:
      if not mp[num]:
        mp[num] = mp[num - 1] + mp[num + 1] + 1
        mp[num - mp[num - 1]] = mp[num]
        mp[num + mp[num + 1]] = mp[num]
        res = max(res, mp[num])
    return res


if __name__ == "__main__":
  TestCase = Solution()

  nums1 = [2, 20, 4, 10, 3, 4, 5]
  Result1 = TestCase.longestConsecutive(nums1)
  print(Result1)

  nums2 = [1, 4, 5, 6, 7, 9, 100, 2, 3, 6, 8]
  Result2 = TestCase.longestConsecutive(nums2)
  print(Result2)
"""
排序, 然后数
"""
