"""
Tests for Chapter4 - Binary Search problems
"""
import importlib.util
import os
import sys

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

  # Try to find the main class - could be Solution, MinStack, TimeMap, etc.
  if 'Solution' in module_dict:
    return module_dict['Solution']
  elif 'MinStack' in module_dict:
    return module_dict['MinStack']
  elif 'TimeMap' in module_dict:
    return module_dict['TimeMap']
  else:
    # Return the first class found
    for key, value in module_dict.items():
      if isinstance(value, type):
        return value
    raise ValueError(f"No class found in {file_path}")


# Load all Solution classes
base_path = "/Users/silverhand/Developer/SourceRepo/LeetCodeProblem/Chapter4-BinarySearch"
BinarySearchSolution = load_solution_from_file(
    f"{base_path}/1-BinarySearch.py")
Search2DMatrixSolution = load_solution_from_file(
    f"{base_path}/2-Search2DMatrix.py")
KokoEatingBananaSolution = load_solution_from_file(
    f"{base_path}/3-KokoEatingBanana.py")
FindMinimumInRotatedSortedArraySolution = load_solution_from_file(
    f"{base_path}/4-FindMinimumInRotatedSortedArray.py")
SearchInRotatedArraySolution = load_solution_from_file(
    f"{base_path}/5-SearchInrRotatedArray.py")
TimeBasedKeyValueStoreSolution = load_solution_from_file(
    f"{base_path}/6-TimeBasedKeyValueStore.py")
MedianOfTwoSortedArraysSolution = load_solution_from_file(
    f"{base_path}/7-MedianOfTwoSortedArrays.py")


class TestBinarySearch:

  def setup_method(self):
    self.solution = BinarySearchSolution()

  def test_binary_search_found(self):
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = self.solution.search(nums, target)
    assert result == 4

  def test_binary_search_not_found(self):
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    result = self.solution.search(nums, target)
    assert result == -1

  def test_binary_search_single_element_found(self):
    nums = [5]
    target = 5
    result = self.solution.search(nums, target)
    assert result == 0

  def test_binary_search_single_element_not_found(self):
    nums = [5]
    target = -5
    result = self.solution.search(nums, target)
    assert result == -1


class TestSearch2DMatrix:

  def setup_method(self):
    self.solution = Search2DMatrixSolution()

  def test_search_2d_matrix_found(self):
    matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]]
    target = 5
    result = self.solution.searchMatrix(matrix, target)
    assert result == True

  def test_search_2d_matrix_not_found(self):
    matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]]
    target = 13
    result = self.solution.searchMatrix(matrix, target)
    assert result == False

  def test_search_2d_matrix_empty(self):
    matrix = []
    target = 1
    result = self.solution.searchMatrix(matrix, target)
    assert result == False


class TestKokoEatingBanana:

  def setup_method(self):
    self.solution = KokoEatingBananaSolution()

  def test_koko_eating_banana_basic(self):
    piles = [3, 6, 7, 11]
    h = 8
    result = self.solution.minEatingSpeed(piles, h)
    assert result == 4

  def test_koko_eating_banana_tight_time(self):
    piles = [30, 11, 23, 4, 20]
    h = 5
    result = self.solution.minEatingSpeed(piles, h)
    assert result == 30

  def test_koko_eating_banana_plenty_time(self):
    piles = [30, 11, 23, 4, 20]
    h = 6
    result = self.solution.minEatingSpeed(piles, h)
    assert result == 23


class TestFindMinimumInRotatedSortedArray:

  def setup_method(self):
    self.solution = FindMinimumInRotatedSortedArraySolution()

  def test_find_minimum_rotated(self):
    nums = [3, 4, 5, 1, 2]
    result = self.solution.findMin(nums)
    assert result == 1

  def test_find_minimum_not_rotated(self):
    nums = [1, 2, 3, 4, 5]
    result = self.solution.findMin(nums)
    assert result == 1

  def test_find_minimum_single_element(self):
    nums = [1]
    result = self.solution.findMin(nums)
    assert result == 1

  def test_find_minimum_two_elements(self):
    nums = [2, 1]
    result = self.solution.findMin(nums)
    assert result == 1


class TestSearchInRotatedArray:

  def setup_method(self):
    self.solution = SearchInRotatedArraySolution()

  def test_search_rotated_array_found(self):
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    result = self.solution.search(nums, target)
    assert result == 4

  def test_search_rotated_array_not_found(self):
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    result = self.solution.search(nums, target)
    assert result == -1

  def test_search_rotated_array_single(self):
    nums = [1]
    target = 0
    result = self.solution.search(nums, target)
    assert result == -1


class TestTimeBasedKeyValueStore:

  def test_time_based_key_value_store(self):
    # Test the TimeMap class directly
    time_map = TimeBasedKeyValueStoreSolution()
    time_map.set("foo", "bar", 1)
    assert time_map.get("foo", 1) == "bar"
    assert time_map.get("foo", 3) == "bar"
    time_map.set("foo", "bar2", 4)
    assert time_map.get("foo", 4) == "bar2"
    assert time_map.get("foo", 5) == "bar2"

  def test_time_based_empty_key(self):
    time_map = TimeBasedKeyValueStoreSolution()
    assert time_map.get("nonexistent", 1) == ""

  def test_time_based_timestamp_order(self):
    time_map = TimeBasedKeyValueStoreSolution()
    time_map.set("love", "high", 10)
    time_map.set("love", "low", 20)
    assert time_map.get("love", 5) == ""
    assert time_map.get("love", 10) == "high"
    assert time_map.get("love", 15) == "high"
    assert time_map.get("love", 20) == "low"
    assert time_map.get("love", 25) == "low"


class TestMedianOfTwoSortedArrays:

  def setup_method(self):
    self.solution = MedianOfTwoSortedArraysSolution()

  def test_median_two_sorted_arrays_odd_total(self):
    nums1 = [1, 3]
    nums2 = [2]
    result = self.solution.findMedianSortedArrays(nums1, nums2)
    assert result == 2.0

  def test_median_two_sorted_arrays_even_total(self):
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = self.solution.findMedianSortedArrays(nums1, nums2)
    assert result == 2.5

  def test_median_two_sorted_arrays_empty_first(self):
    nums1 = []
    nums2 = [1]
    result = self.solution.findMedianSortedArrays(nums1, nums2)
    assert result == 1.0

  def test_median_two_sorted_arrays_different_sizes(self):
    nums1 = [0, 0]
    nums2 = [0, 0]
    result = self.solution.findMedianSortedArrays(nums1, nums2)
    assert result == 0.0
