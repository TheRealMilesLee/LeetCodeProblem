"""
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn)O(logn) time.
"""


class Solution:

  def search(self, nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
      middle = left + ((right - left) // 2)

      if nums[middle] < target:
        left = middle + 1
      elif nums[middle] > target:
        right = middle - 1
      else:
        return middle
    return -1


if __name__ == '__main__':
  TestCase = Solution()
  nums = [-1, 0, 2, 4, 6, 8]
  Result1 = TestCase.search(nums, 4)
  print(Result1)
"""
经典二分查找, 从中间开始, 小了就把左边的挪到中间, 大了就把右边的挪到中间, 找不到就直接返回-1
"""
