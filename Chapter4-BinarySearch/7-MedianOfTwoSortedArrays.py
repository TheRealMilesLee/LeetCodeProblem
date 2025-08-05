"""
You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

Your solution must run in O(log(m+n))O(log(m+n)) time.
"""


class Solution:

  def findMedianSortedArrays(self, nums1: list[int],
                             nums2: list[int]) -> float:
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
      A, B = B, A

    left, right = 0, len(A) - 1
    while True:
      i = (left + right) // 2
      j = half - i - 2

      if i >= 0:
        Aleft = A[i]
      else:
        Aleft = float("infinity")

      if (i + 1) < len(A):
        Aright = A[i + 1]
      else:
        Aright = float("infinity")

      if j >= 0:
        Bleft = B[j]
      else:
        Bleft = float("-infinity")
      Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

      if Aleft <= Bright and Bleft <= Aright:
        if total % 2:
          return min(Aright, Bright)
        return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
      elif Aleft > Bright:
        right = i - 1
      else:
        left = i + 1


if __name__ == '__main__':
  TestCase = Solution()

  nums1 = [1, 2]
  nums2 = [3]
  Result1 = TestCase.findMedianSortedArrays(nums1, nums2)
  print(Result1)
