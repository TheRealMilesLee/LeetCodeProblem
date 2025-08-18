"""
Tests for Chapter1 - Array Hashing problems
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import importlib.util

import pytest


def load_solution_from_file(file_path):
  """Load Solution class from a Python file"""
  import sys
  from io import StringIO

  # Read the file content
  with open(file_path, 'r') as f:
    content = f.read()

  # Create a module namespace
  module_dict = {}

  # Capture stdout to suppress any print statements in the main block
  old_stdout = sys.stdout
  sys.stdout = StringIO()

  try:
    # Execute only the class definition part, not the main block
    lines = content.split('\n')
    class_lines = []
    in_main = False

    for line in lines:
      if line.strip().startswith('if __name__ == "__main__"'):
        in_main = True
        break
      if not in_main:
        class_lines.append(line)

    class_content = '\n'.join(class_lines)
    exec(class_content, module_dict)

  finally:
    # Restore stdout
    sys.stdout = old_stdout

  return module_dict['Solution']


# Load all Solution classes
base_path = "/Users/silverhand/Developer/SourceRepo/LeetCodeProblem/Chapter1-ArrayHashing"
ContainsDuplicateSolution = load_solution_from_file(
    f"{base_path}/1-ContainsDuplicate.py")
ValidAnagramSolution = load_solution_from_file(
    f"{base_path}/2-ValidAnagram.py")
TwoSumSolution = load_solution_from_file(f"{base_path}/3-TwoSum.py")
GroupAnagramsSolution = load_solution_from_file(
    f"{base_path}/4-GroupAnagrams.py")
TopKFrequentSolution = load_solution_from_file(
    f"{base_path}/5-TopKFrequent.py")
EncodeDecodeSolution = load_solution_from_file(
    f"{base_path}/6-EncodeDecodeString.py")
ProductOfArraySolution = load_solution_from_file(
    f"{base_path}/7-ProductOfArray.py")
ValidSudokuSolution = load_solution_from_file(f"{base_path}/8-ValidSudoku.py")
LongestCommonSequenceSolution = load_solution_from_file(
    f"{base_path}/9-LongestCommonSequence.py")


class TestContainsDuplicate:

  def setup_method(self):
    self.solution = ContainsDuplicateSolution()

  def test_contains_duplicate_true(self):
    nums = [1, 2, 3, 3]
    assert self.solution.hasDuplicate(nums) == True

  def test_contains_duplicate_false(self):
    nums = [1, 2, 3, 4]
    assert self.solution.hasDuplicate(nums) == False

  def test_empty_array(self):
    nums = []
    assert self.solution.hasDuplicate(nums) == False

  def test_single_element(self):
    nums = [1]
    assert self.solution.hasDuplicate(nums) == False


class TestValidAnagram:

  def setup_method(self):
    self.solution = ValidAnagramSolution()

  def test_valid_anagram(self):
    s = "anagram"
    t = "nagaram"
    assert self.solution.isAnagram(s, t) == True

  def test_invalid_anagram(self):
    s = "rat"
    t = "car"
    assert self.solution.isAnagram(s, t) == False

  def test_different_length(self):
    s = "abc"
    t = "abcd"
    assert self.solution.isAnagram(s, t) == False

  def test_empty_strings(self):
    s = ""
    t = ""
    assert self.solution.isAnagram(s, t) == True


class TestTwoSum:

  def setup_method(self):
    self.solution = TwoSumSolution()

  def test_two_sum_basic(self):
    nums = [2, 7, 11, 15]
    target = 9
    result = self.solution.twoSum(nums, target)
    assert sorted(result) == [0, 1]

  def test_two_sum_negative(self):
    nums = [3, 2, 4]
    target = 6
    result = self.solution.twoSum(nums, target)
    assert sorted(result) == [1, 2]

  def test_two_sum_duplicates(self):
    nums = [3, 3]
    target = 6
    result = self.solution.twoSum(nums, target)
    assert sorted(result) == [0, 1]


class TestGroupAnagrams:

  def setup_method(self):
    self.solution = GroupAnagramsSolution()

  def test_group_anagrams_basic(self):
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = self.solution.groupAnagrams(strs)
    # Sort each group and then sort the groups for comparison
    result_sorted = [sorted(group) for group in result]
    result_sorted.sort()
    expected = [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    expected_sorted = [sorted(group) for group in expected]
    expected_sorted.sort()
    assert result_sorted == expected_sorted

  def test_group_anagrams_empty(self):
    strs = [""]
    result = self.solution.groupAnagrams(strs)
    assert result == [[""]]

  def test_group_anagrams_single(self):
    strs = ["a"]
    result = self.solution.groupAnagrams(strs)
    assert result == [["a"]]


class TestTopKFrequent:

  def setup_method(self):
    self.solution = TopKFrequentSolution()

  def test_top_k_frequent_basic(self):
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = self.solution.topKFrequent(nums, k)
    assert sorted(result) == [1, 2]

  def test_top_k_frequent_single(self):
    nums = [1]
    k = 1
    result = self.solution.topKFrequent(nums, k)
    assert result == [1]


class TestEncodeDecodeString:

  def setup_method(self):
    self.solution = EncodeDecodeSolution()

  def test_encode_decode_basic(self):
    strs = ["hello", "world"]
    encoded = self.solution.encode(strs)
    decoded = self.solution.decode(encoded)
    assert decoded == strs

  def test_encode_decode_empty_strings(self):
    strs = ["", ""]
    encoded = self.solution.encode(strs)
    decoded = self.solution.decode(encoded)
    assert decoded == strs

  def test_encode_decode_special_chars(self):
    strs = ["hello#world", "test"]
    encoded = self.solution.encode(strs)
    decoded = self.solution.decode(encoded)
    assert decoded == strs


class TestProductOfArray:

  def setup_method(self):
    self.solution = ProductOfArraySolution()

  def test_product_of_array_basic(self):
    nums = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]
    assert self.solution.productExceptSelf(nums) == expected

  def test_product_of_array_with_zero(self):
    nums = [-1, 1, 0, -3, 3]
    expected = [0, 0, 9, 0, 0]
    assert self.solution.productExceptSelf(nums) == expected


class TestValidSudoku:

  def setup_method(self):
    self.solution = ValidSudokuSolution()

  def test_valid_sudoku_true(self):
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert self.solution.isValidSudoku(board) == True

  def test_valid_sudoku_false(self):
    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert self.solution.isValidSudoku(board) == False


class TestLongestCommonSequence:

  def setup_method(self):
    self.solution = LongestCommonSequenceSolution()

  def test_longest_consecutive_basic(self):
    nums = [100, 4, 200, 1, 3, 2]
    assert self.solution.longestConsecutive(nums) == 4

  def test_longest_consecutive_empty(self):
    nums = []
    assert self.solution.longestConsecutive(nums) == 0

  def test_longest_consecutive_single(self):
    nums = [1]
    assert self.solution.longestConsecutive(nums) == 1
