"""
Give an array of integers numbers that is sorted in non-decreasing order

Return the indices (1-indexed) of two numbers such that they add up to a given
target number and index1 < index2. Note that index 1 and index2 cannot be equal, you may NOT use the same element twice

There will always be exactly one valid solution, you solution must use O(1) additional space
"""


class Solution:

  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    ptrLeft = 0
    ptrRight = len(numbers) - 1

    while ptrLeft < ptrRight:
      currentSum = numbers[ptrLeft] + numbers[ptrRight]
      if currentSum > target:
        ptrRight -= 1
      elif currentSum < target:
        ptrLeft += 1
      else:
        return [ptrLeft + 1, ptrRight + 1]
    return []


if __name__ == "__main__":
  TestCase = Solution()

  nums1 = [1, 2, 3, 4]
  target = 3
  Result1 = TestCase.twoSum(nums1, target)
  print(Result1)


"""
思路核心还是双指针, 还是一头一尾. 如果左右加起来大于target, 那么说明右边数字大了, 如果小于target说明左边数字小了, 然后就分别移动就好

突破点在于题目中说的array已经排好序了, 并且不会出现相同数字的情况
"""
