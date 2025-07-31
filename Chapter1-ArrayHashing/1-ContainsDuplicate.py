"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false
"""


class Solution:

  def hasDuplicate(self, nums: list[int]) -> bool:
    records = set()

    for index in nums:
      if index in records:
        return True
      else:
        records.add(index)
    return False


if __name__ == "__main__":
  TestCase = Solution()
  nums1 = [1, 2, 3, 3]
  nums2 = [1, 2, 3, 4]

  results1 = TestCase.hasDuplicate(nums1)
  print(results1)

  results2 = TestCase.hasDuplicate(nums2)
  print(results2)
"""
实际上就是查重, set就可以去重, 那么如果当前的在set里面出现了,则可以直接return true, 如果没有出现就把当前的加入进去
"""
