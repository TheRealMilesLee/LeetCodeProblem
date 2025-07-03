"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false
"""
import collections


def solution(nums: list[int]) -> bool:
  myDict = collections.defaultdict()
  for index in nums:
    if index not in myDict:
      myDict[index] = 1
    else:
      myDict[index] += 1

  for _, values in myDict.items():
    if values > 1:
      return True
  return False


if __name__ == "__main__":
  nums1 = [1, 2, 3, 3]
  nums2 = [1, 2, 3, 4]

  results1 = solution(nums1)
  print(results1)

  results2 = solution(nums2)
  print(results2)
