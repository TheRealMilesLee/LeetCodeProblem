"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false
"""
import collections


class Solution:

  def hasDuplicate(self, nums: list[int]) -> bool:
    appearTime = collections.defaultdict()
    for index in nums:
      if int(index) not in appearTime.keys():
        appearTime[int(index)] = 1
      else:
        appearTime[int(index)] += 1
        return True
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
最简单的方式就是用Hashmap, Key是nums里的数, value是出现的次数。
先检查是否已经在hashmap里面存在, 如果已经存在就可以+1然后直接return true, 如果不存在则加入
到当前的Hashmap中
"""
