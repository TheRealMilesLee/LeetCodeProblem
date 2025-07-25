"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""


class Solution:

  def twoSum(self, nums: list[int], target: int) -> list[int]:
    prevMap = {}

    for index, number in enumerate(nums):
      diff = target - number
      if diff in prevMap:
        return [prevMap[diff], index]
      prevMap[number] = index


if __name__ == "__main__":
  TestCase = Solution()

  nums1 = [3, 4, 5, 6]
  nums2 = [4, 5, 6]

  results1 = TestCase.twoSum(nums1, 7)
  print(results1)

  results2 = TestCase.twoSum(nums2, 10)
  print(results2)
