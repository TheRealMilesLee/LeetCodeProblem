"""
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

    [3,4,5,6,1,2] if it was rotated 4 times.
    [1,2,3,4,5,6] if it was rotated 6 times.

Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
"""


class Solution:

  def search(self, nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
      mid = (l + r) // 2
      if target == nums[mid]:
        return mid

      if nums[l] <= nums[mid]:
        if target > nums[mid] or target < nums[l]:
          l = mid + 1
        else:
          r = mid - 1

      else:
        if target < nums[mid] or target > nums[r]:
          r = mid - 1
        else:
          l = mid + 1
    return -1


if __name__ == '__main__':
  TestCase = Solution()

  nums = [3, 4, 5, 6, 1, 2]
  Result1 = TestCase.search(nums)
  print(Result1)
