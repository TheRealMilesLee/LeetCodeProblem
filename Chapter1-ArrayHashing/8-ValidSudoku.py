"""
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

- Each row must contain the digits 1-9 without duplicates.
- Each column must contain the digits 1-9 without duplicates.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

Return true if the Sudoku board is valid, otherwise return false
"""
import collections


class Solution:

  def isValidSudoku(self, board: list[list[str]]) -> bool:
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for column in range(9):
      for row in range(9):
        if board[row][column] != ".":
          if (board[row][column] in rows[row]
              or board[row][column] in cols[column]
              or board[row][column] in squares[(row // 3, column // 3)]):
            return False
          cols[column].add(board[row][column])
          rows[row].add(board[row][column])
          squares[(row // 3, column // 3)].add(board[row][column])
    return True


if __name__ == "__main__":
  TestCase = Solution()

  board1 = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
Result1 = TestCase.isValidSudoku(board1)
print(Result1)

board2 = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
          ["4", ".", ".", "5", ".", ".", ".", ".", "."],
          [".", "9", "1", ".", ".", ".", ".", ".", "3"],
          ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
          [".", ".", ".", "8", ".", "3", ".", ".", "5"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", ".", ".", ".", ".", ".", "2", ".", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "8"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

Result2 = TestCase.isValidSudoku(board2)
print(Result2)

"""
没啥复杂的, 就是hashmap存了然后看在不在就完事了
"""
