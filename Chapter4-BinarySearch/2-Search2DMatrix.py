"""
You are given an m x n 2-D integer array matrix and an integer target.

    Each row in matrix is sorted in non-decreasing order.
    The first integer of every row is greater than the last integer of the previous row.

Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?
"""


class Solution:

  def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    row = len(matrix)
    col = len(matrix[0])

    left = 0
    right = row * col - 1

    while left <= right:
      middle = left + (right - left) // 2

      indexRow = middle // col
      indexCol = middle % col

      if target > matrix[indexRow][indexCol]:
        left = middle + 1
      elif target < matrix[indexRow][indexCol]:
        right = middle - 1
      else:
        return True
    return False


if __name__ == '__main__':
  TestCase = Solution()
  matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
  Result1 = TestCase.searchMatrix(matrix1, 3)
  print(Result1)

  matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
  Result2 = TestCase.searchMatrix(matrix2, 13)
  print(Result2)

"""
二分法的变体, 这次的思路是先二分法定位target所在的row的区间, 然后再把这个区间单独提出来再执行一遍二分法来找这个数, 如果找不到就直接return false

因为题中说了row是排序了的, 并且上一个row一定比下一个row小, 那么就可以用这个方法来进行定位
"""
