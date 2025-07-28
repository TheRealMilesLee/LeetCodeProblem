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

  def productExceptFaster(self, nums: list[int]) -> list[int]:
    length = len(nums)
    result = [1] * length

    # 左乘积
    left_product = 1
    for i in range(length):
      result[i] = left_product
      left_product *= nums[i]

    # 右乘积
    right_product = 1
    for i in range(length - 1, -1, -1):
      result[i] *= right_product
      right_product *= nums[i]

    return result


if __name__ == "__main__":
  TestCase = Solution()

  Array1 = [1, 2, 4, 6]
  Result1 = TestCase.productExceptItSelf(Array1)
  Better1 = TestCase.productExceptFaster(Array1)
  print(f"{Result1} {Better1} \n")

  Array2 = [-1, 0, 1, 2, 3]
  Result2 = TestCase.productExceptItSelf(Array2)
  Better2 = TestCase.productExceptFaster(Array2)
  print(f"{Result2} {Better2} \n")

  Array3 = [1, 3, 5, 7]
  Result3 = TestCase.productExceptItSelf(Array3)
  Better3 = TestCase.productExceptFaster(Array3)
  print(f"{Result3} {Better3} \n")

  Array4 = [9, -9, 0, 1]
  Result4 = TestCase.productExceptItSelf(Array4)
  Better4 = TestCase.productExceptFaster(Array4)
  print(f"{Result4} {Better4} \n")
