"""
Tests for Chapter2 - Two Pointer problems
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

  return module_dict['Solution']


# Load all Solution classes
base_path = "/Users/silverhand/Developer/SourceRepo/LeetCodeProblem/Chapter2-TwoPointer"
ValidPalindromeSolution = load_solution_from_file(
    f"{base_path}/1-ValiPalindrome.py")
TwoIntegerSumSolution = load_solution_from_file(
    f"{base_path}/2-TwoIntegerSum.py")
ThreeSumSolution = load_solution_from_file(f"{base_path}/3-ThreeSum.py")
ContainerWithMostWaterSolution = load_solution_from_file(
    f"{base_path}/4-ContainerWithMostWater.py")
TrappingRainWaterSolution = load_solution_from_file(
    f"{base_path}/5-TrappingRainWatere.py")


class TestValidPalindrome:

  def setup_method(self):
    self.solution = ValidPalindromeSolution()

  def test_valid_palindrome_true(self):
    s = "Was it a car or a cat I saw?"
    assert self.solution.isPalindrome(s) == True

  def test_valid_palindrome_false(self):
    s = "tab a cat"
    assert self.solution.isPalindrome(s) == False

  def test_empty_string(self):
    s = ""
    assert self.solution.isPalindrome(s) == True

  def test_single_character(self):
    s = "a"
    assert self.solution.isPalindrome(s) == True

  def test_alphanumeric_only(self):
    s = "A man a plan a canal Panama"
    assert self.solution.isPalindrome(s) == True


class TestTwoIntegerSum:

  def setup_method(self):
    self.solution = TwoIntegerSumSolution()

  def test_two_integer_sum_basic(self):
    numbers = [1, 2, 3, 4]
    target = 3
    result = self.solution.twoSum(numbers, target)
    assert result == [1, 2]

  def test_two_integer_sum_larger(self):
    numbers = [1, 3, 4, 5, 7, 10, 11]
    target = 9
    result = self.solution.twoSum(numbers, target)
    assert result == [3, 4]

  def test_two_integer_sum_negative(self):
    numbers = [-1, 0, 1, 2]
    target = 1
    result = self.solution.twoSum(numbers, target)
    assert result == [2, 3]


class TestThreeSum:

  def setup_method(self):
    self.solution = ThreeSumSolution()

  def test_three_sum_basic(self):
    nums = [-1, 0, 1, 2, -1, -4]
    result = self.solution.threeSum(nums)
    expected = [[-1, -1, 2], [-1, 0, 1]]
    # Sort the results for comparison since order may vary
    result_sorted = [sorted(triplet) for triplet in result]
    result_sorted.sort()
    expected_sorted = [sorted(triplet) for triplet in expected]
    expected_sorted.sort()
    assert result_sorted == expected_sorted

  def test_three_sum_no_solution(self):
    nums = [0, 1, 1]
    result = self.solution.threeSum(nums)
    assert result == []

  def test_three_sum_all_zeros(self):
    nums = [0, 0, 0]
    result = self.solution.threeSum(nums)
    assert result == [[0, 0, 0]]


class TestContainerWithMostWater:

  def setup_method(self):
    self.solution = ContainerWithMostWaterSolution()

  def test_container_basic(self):
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = self.solution.maxArea(height)
    assert result == 49

  def test_container_two_elements(self):
    height = [1, 1]
    result = self.solution.maxArea(height)
    assert result == 1

  def test_container_ascending(self):
    height = [1, 2, 3, 4, 5]
    result = self.solution.maxArea(height)
    assert result == 6


class TestTrappingRainWater:

  def setup_method(self):
    self.solution = TrappingRainWaterSolution()

  def test_trapping_rain_water_basic(self):
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = self.solution.trap(height)
    assert result == 6

  def test_trapping_rain_water_no_trap(self):
    height = [3, 0, 2, 0, 4]
    result = self.solution.trap(height)
    assert result == 7

  def test_trapping_rain_water_empty(self):
    height = []
    result = self.solution.trap(height)
    assert result == 0

  def test_trapping_rain_water_flat(self):
    height = [1, 1, 1, 1]
    result = self.solution.trap(height)
    assert result == 0
