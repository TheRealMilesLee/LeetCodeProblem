"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
"""


class Solution:

  def threeSum(self, nums: list[int]) -> list[list[int]]:
    results = []
    nums.sort()

    for index, middle in enumerate(nums):
      if middle > 0:
        break
      if index > 0 and middle == nums[index - 1]:
        continue

      left = index + 1
      right = len(nums) - 1

      while left < right:
        threesum = middle + nums[left] + nums[right]
        if threesum > 0:
          right -= 1
        elif threesum < 0:
          left += 1
        else:
          results.append([middle, nums[left], nums[right]])
          left += 1
          right -= 1
          while nums[left] == nums[left - 1] and left < right:
            left += 1
    return results


if __name__ == "__main__":
  TestCase = Solution()

  nums1 = [-1, 0, 1, 2, -1, -4]
  Result1 = TestCase.threeSum(nums1)
  print(Result1)

  nums2 = [0, 1, 1]
  Result2 = TestCase.threeSum(nums2)
  print(Result2)
"""
和之前的Two Sum 很像，只不过这次是三个数，那我们就以中间的数为起点, 然后正常做双指针就好

e.g.

nums = [-4, -1, -1, 0, 1, 2]

那么第一个middle = -4, 然后left就是 -1, right就是-1这样的双指针向前走, 然后middle为 -1, left为-1, right 为0, 继续这样
"""
