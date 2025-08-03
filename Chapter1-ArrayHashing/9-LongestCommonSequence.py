"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.
"""


class Solution:

  def longestConsecutive(self, nums: list[int]) -> int:
    numSet = set(nums)
    longest = 0

    for num in numSet:
      # find the start of the sequence
      if (num - 1) not in numSet:
        length = 1
        # Count the current lenghth of the sequence
        while (num + length) in numSet:
          length += 1
        longest = max(length, longest)
    return longest

  def longestConsecutiveSlower(self, nums: list[int]) -> int:
    if not nums:
      return 0

    nums.sort()
    longest = 1
    currentLength = 1

    for i in range(1, len(nums)):
      if nums[i] == nums[i - 1]:
        continue  # 跳过重复的数字
      elif nums[i] == nums[i - 1] + 1:
        currentLength += 1
      else:
        currentLength = 1  # 断掉了，重新开始
      longest = max(longest, currentLength)

    return longest


if __name__ == "__main__":
  TestCase = Solution()

  nums1 = [2, 20, 4, 10, 3, 4, 5]
  Result1 = TestCase.longestConsecutive(nums1)
  ResultSlower = TestCase.longestConsecutiveSlower(nums1)
  print(Result1)
  print(ResultSlower)

  nums2 = [1, 4, 5, 6, 7, 9, 100, 2, 3, 6, 8]
  Result2 = TestCase.longestConsecutive(nums2)
  ResultSlower2 = TestCase.longestConsecutiveSlower(nums2)
  print(Result2)
  print(ResultSlower2)
"""
这个题Tricky的地方在于如何去判断sequence. 总结下来其实就是先找到sequence的起点, 然后看当前数字的下一个数在不在nums里, 如果在就直接往下加
"""
