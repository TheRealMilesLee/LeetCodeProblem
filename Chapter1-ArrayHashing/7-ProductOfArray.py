"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i]

Each product is guaranteed to fit in a 32 bit integer

Could you solve it in O(n) time without using the division operation
"""


class Solution:

  def productExceptSelf(self, nums: list[int]) -> list[int]:
    n = len(nums)
    res = [0] * n
    pref = [0] * n
    suff = [0] * n

    pref[0] = suff[n - 1] = 1
    for i in range(1, n):
      pref[i] = nums[i - 1] * pref[i - 1]
    for i in range(n - 2, -1, -1):
      suff[i] = nums[i + 1] * suff[i + 1]
    for i in range(n):
      res[i] = pref[i] * suff[i]
    return res


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

"""
用L形的方法将 nums和prefix相乘, 然后放入下一个index, 然后再把L倒过来, 从最后往前面乘, 结果放入上一位

nums:   1   2   4   6
prefix: 1   1   2   8
suffix: 48  24  6   1

最后再把prefix和suffix相乘
48  24  12  8
得到最后结果
"""
