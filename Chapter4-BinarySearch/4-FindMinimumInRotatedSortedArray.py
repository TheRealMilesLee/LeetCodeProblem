"""
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

    [3,4,5,6,1,2] if it was rotated 4 times.
    [1,2,3,4,5,6] if it was rotated 6 times.

Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
"""


class Solution:

  def finMin(self, nums: list[int]) -> int:
    results = nums[0]

    left = 0
    right = len(nums) - 1

    while left <= right:
      if nums[left] < nums[right]:
        results = min(results, nums[left])
        break

      middle = (left + right) // 2
      results = min(results, nums[middle])

      if nums[0] >= nums[left]:
        left = middle + 1
      else:
        right = middle - 1
    return results


if __name__ == '__main__':
  TestCase = Solution()

  nums = [3, 4, 5, 6, 1, 2]
  Result1 = TestCase.finMin(nums)
  print(Result1)

  nums2 = [4, 5, 0, 1, 2, 3]
  Result2 = TestCase.finMin(nums2)
  print(Result2)
"""
如果是已经排序的Array, 那么直接return第一个数就好. 但是这里是旋转以后的, 所以我们这还是可以从中间开始, 如果中间的数大于最左边的, 那么左半边的就可以不管了只看右边, 如果中间的数小于左边的, 那么右半边的就可以不管了只看左半边, 而因为原来的array是排序过的, 所以左半边和右半边也一定是有序的

i.e. 就是看array是往左rotate还是往右rotate
"""
