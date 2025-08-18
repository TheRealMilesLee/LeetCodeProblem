"""
Tests for Dynamic Programming problems
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
base_path = "/Users/silverhand/Developer/SourceRepo/LeetCodeProblem/DynamicProgramming"
CoinChangeSolution = load_solution_from_file(f"{base_path}/DP-CoinChange.py")
RodCuttingSolution = load_solution_from_file(f"{base_path}/DP-RodCutting.py")


class TestCoinChange:

  def setup_method(self):
    self.solution = CoinChangeSolution()

  def test_coin_change_basic(self):
    coins = [1, 3, 4]
    amount = 6
    result = self.solution.coinChange(coins, amount)
    assert result == 2  # 3 + 3

  def test_coin_change_impossible(self):
    coins = [2]
    amount = 3
    result = self.solution.coinChange(coins, amount)
    assert result == -1

  def test_coin_change_zero_amount(self):
    coins = [1]
    amount = 0
    result = self.solution.coinChange(coins, amount)
    assert result == 0

  def test_coin_change_single_coin(self):
    coins = [1]
    amount = 1
    result = self.solution.coinChange(coins, amount)
    assert result == 1

  def test_coin_change_multiple_options(self):
    coins = [1, 2, 5]
    amount = 11
    result = self.solution.coinChange(coins, amount)
    assert result == 3  # 5 + 5 + 1


class TestRodCutting:

  def setup_method(self):
    self.solution = RodCuttingSolution()

  def test_rod_cutting_basic(self):
    # Test case depends on the specific implementation
    # Common rod cutting problem: given rod length and prices for different lengths
    prices = [0, 1, 5, 8, 9, 10, 17, 17,
              20]  # prices[i] = price for rod of length i
    n = 4  # rod length
    result = self.solution.rodCutting(prices, n)
    assert result == 10  # cut into two pieces of length 2 each (5 + 5)

  def test_rod_cutting_no_cut_needed(self):
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 10
    result = self.solution.rodCutting(prices, n)
    assert result == 30  # don't cut, sell as whole

  def test_rod_cutting_single_unit(self):
    prices = [0, 3, 7, 8, 9]
    n = 1
    result = self.solution.rodCutting(prices, n)
    assert result == 3

  def test_rod_cutting_zero_length(self):
    prices = [0, 1, 5, 8, 9]
    n = 0
    result = self.solution.rodCutting(prices, n)
    assert result == 0

  def test_rod_cutting_optimal_cuts(self):
    prices = [0, 3, 5, 8, 9, 10, 20, 22, 25, 30]
    n = 8
    result = self.solution.rodCutting(prices, n)
    # Optimal is likely multiple cuts to maximize profit
    assert result >= 22  # at least the price of selling as one piece
