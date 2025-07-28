"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i]

Each product is guaranteed to fit in a 32 bit integer

Could you solve it in O(n) time without using the division operation
"""


class Solution:

  def productExceptItSelf(self, nums: list[int]) -> list[int]:
    resultArray = []

    for index in range(len(nums)):
      product = 1
      for multi in range(len(nums)):
        if index != multi:
          product *= nums[multi]
      resultArray.append(product)
    return resultArray


if __name__ == "__main__":
  TestCase = Solution()

  Array1 = [1, 2, 4, 6]
  Result1 = TestCase.productExceptItSelf(Array1)
  print(Result1)

  Array2 = [-1, 0, 1, 2, 3]
  Result2 = TestCase.productExceptItSelf(Array2)
  print(Result2)

  Array3 = [1, 3, 5, 7]
  Result3 = TestCase.productExceptItSelf(Array3)
  print(Result3)

  Array4 = [9, -9, 0, 1]
  Result4 = TestCase.productExceptItSelf(Array4)
  print(Result4)
