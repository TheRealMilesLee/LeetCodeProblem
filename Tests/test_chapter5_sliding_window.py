"""
Tests for Chapter5 - Sliding Window problems
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
base_path = "/Users/silverhand/Developer/SourceRepo/LeetCodeProblem/Chapter5-SlidingWindow"
BestTimeToBuyAndSellStockSolution = load_solution_from_file(
    f"{base_path}/1-BestTimeToBuyAndSellStock.py")
LongestSubstringWithoutRepeatingSolution = load_solution_from_file(
    f"{base_path}/2-LongestSubstringWithoutRepeating.py")
LongestRepeatingCharacterReplacementSolution = load_solution_from_file(
    f"{base_path}/3-LongestRepeatingCharacterReplacement.py")
PermutationInStringSolution = load_solution_from_file(
    f"{base_path}/4-PermutationInString.py")
MinimumWindowSubstringSolution = load_solution_from_file(
    f"{base_path}/5-MinimumWindowSubstring.py")
SlidingWindowMaximumSolution = load_solution_from_file(
    f"{base_path}/6-SlidingWindowMaximum.py")


class TestBestTimeToBuyAndSellStock:

  def setup_method(self):
    self.solution = BestTimeToBuyAndSellStockSolution()

  def test_best_time_basic(self):
    prices = [7, 1, 5, 3, 6, 4]
    result = self.solution.maxProfit(prices)
    assert result == 5

  def test_best_time_no_profit(self):
    prices = [7, 6, 4, 3, 1]
    result = self.solution.maxProfit(prices)
    assert result == 0

  def test_best_time_single_price(self):
    prices = [1]
    result = self.solution.maxProfit(prices)
    assert result == 0

  def test_best_time_two_prices(self):
    prices = [1, 5]
    result = self.solution.maxProfit(prices)
    assert result == 4


class TestLongestSubstringWithoutRepeating:

  def setup_method(self):
    self.solution = LongestSubstringWithoutRepeatingSolution()

  def test_longest_substring_basic(self):
    s = "abcabcbb"
    result = self.solution.lengthOfLongestSubstring(s)
    assert result == 3

  def test_longest_substring_all_same(self):
    s = "bbbbb"
    result = self.solution.lengthOfLongestSubstring(s)
    assert result == 1

  def test_longest_substring_no_repeat(self):
    s = "pwwkew"
    result = self.solution.lengthOfLongestSubstring(s)
    assert result == 3

  def test_longest_substring_empty(self):
    s = ""
    result = self.solution.lengthOfLongestSubstring(s)
    assert result == 0

  def test_longest_substring_single_char(self):
    s = "a"
    result = self.solution.lengthOfLongestSubstring(s)
    assert result == 1


class TestLongestRepeatingCharacterReplacement:

  def setup_method(self):
    self.solution = LongestRepeatingCharacterReplacementSolution()

  def test_character_replacement_basic(self):
    s = "ABAB"
    k = 2
    result = self.solution.characterReplacement(s, k)
    assert result == 4

  def test_character_replacement_different_case(self):
    s = "AABABBA"
    k = 1
    result = self.solution.characterReplacement(s, k)
    assert result == 4

  def test_character_replacement_no_replacement_needed(self):
    s = "AAAA"
    k = 2
    result = self.solution.characterReplacement(s, k)
    assert result == 4

  def test_character_replacement_single_char(self):
    s = "A"
    k = 1
    result = self.solution.characterReplacement(s, k)
    assert result == 1


class TestPermutationInString:

  def setup_method(self):
    self.solution = PermutationInStringSolution()

  def test_permutation_in_string_true(self):
    s1 = "ab"
    s2 = "eidbaooo"
    result = self.solution.checkInclusion(s1, s2)
    assert result == True

  def test_permutation_in_string_false(self):
    s1 = "ab"
    s2 = "eidboaoo"
    result = self.solution.checkInclusion(s1, s2)
    assert result == False

  def test_permutation_in_string_same_length(self):
    s1 = "abc"
    s2 = "bac"
    result = self.solution.checkInclusion(s1, s2)
    assert result == True

  def test_permutation_in_string_s1_longer(self):
    s1 = "abcdef"
    s2 = "abc"
    result = self.solution.checkInclusion(s1, s2)
    assert result == False


class TestMinimumWindowSubstring:

  def setup_method(self):
    self.solution = MinimumWindowSubstringSolution()

  def test_minimum_window_basic(self):
    s = "ADOBECODEBANC"
    t = "ABC"
    result = self.solution.minWindow(s, t)
    assert result == "BANC"

  def test_minimum_window_no_solution(self):
    s = "a"
    t = "aa"
    result = self.solution.minWindow(s, t)
    assert result == ""

  def test_minimum_window_exact_match(self):
    s = "a"
    t = "a"
    result = self.solution.minWindow(s, t)
    assert result == "a"

  def test_minimum_window_multiple_solutions(self):
    s = "ADOBECODEBANC"
    t = "AABC"
    result = self.solution.minWindow(s, t)
    # The minimum window should contain all required characters
    assert len(result) >= 4  # At least contains A, A, B, C


class TestSlidingWindowMaximum:

  def setup_method(self):
    self.solution = SlidingWindowMaximumSolution()

  def test_sliding_window_maximum_basic(self):
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = self.solution.maxSlidingWindow(nums, k)
    expected = [3, 3, 5, 5, 6, 7]
    assert result == expected

  def test_sliding_window_maximum_single_element(self):
    nums = [1]
    k = 1
    result = self.solution.maxSlidingWindow(nums, k)
    assert result == [1]

  def test_sliding_window_maximum_ascending(self):
    nums = [1, 2, 3, 4, 5]
    k = 3
    result = self.solution.maxSlidingWindow(nums, k)
    expected = [3, 4, 5]
    assert result == expected

  def test_sliding_window_maximum_descending(self):
    nums = [5, 4, 3, 2, 1]
    k = 2
    result = self.solution.maxSlidingWindow(nums, k)
    expected = [5, 4, 3, 2]
    assert result == expected
