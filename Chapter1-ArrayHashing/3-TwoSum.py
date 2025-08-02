"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""


class Solution:

  def twoSum(self, nums: list[int], target: int) -> list[int]:
    record = {}

    for index, number in enumerate(nums):
      difference = target - number
      if difference in record:
        return [record[difference], index]
      else:
        record[number] = index


if __name__ == "__main__":
  TestCase = Solution()

  nums1 = [3, 4, 5, 6]
  nums2 = [4, 5, 6]
  nums3 = [1, 3, 4, 2]

  results1 = TestCase.twoSum(nums1, 7)
  print(results1)

  results2 = TestCase.twoSum(nums2, 10)
  print(results2)

  results3 = TestCase.twoSum(nums3, 6)
  print(results3)
"""
最经典的两数之和问题， 要用两个index凑出target, 我们只需要去看另一个index在当前的array中是否存在

比如1 + 3 = 4, 其中4是target, 那么我们只需要去看一下1 和 3 分别在当前array的哪个index上。 所以我们可以用hashmap 来记录这个数据。key是当前数字, 而value是当前数字所在的index

走一个循环遍历整个nums, 用target去减当前number, 然后用这个为search key在hashmap里找到对应的index并且返回
"""
