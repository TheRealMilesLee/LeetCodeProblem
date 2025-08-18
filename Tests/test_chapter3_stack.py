"""
Tests for Chapter3 - Stack problems
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
base_path = "/Users/silverhand/Developer/SourceRepo/LeetCodeProblem/Chapter3-Stack"
ValidParenthesesSolution = load_solution_from_file(
    f"{base_path}/1-ValidParentensis.py")
MinimumStackSolution = load_solution_from_file(
    f"{base_path}/2-MinimumStack.py")
EvaluateReversePolishNotationSolution = load_solution_from_file(
    f"{base_path}/3-EvaluateReversePolishNotation.py")
GenerateParenthesesSolution = load_solution_from_file(
    f"{base_path}/4-GenerateParentheses.py")
DailyTemperaturesSolution = load_solution_from_file(
    f"{base_path}/5-DailyTemperatures.py")
CarFleetSolution = load_solution_from_file(f"{base_path}/6-CarFleet.py")
LargestRectangleInHistogramSolution = load_solution_from_file(
    f"{base_path}/7-LargestRectangleInHistogram.py")


class TestValidParentheses:

  def setup_method(self):
    self.solution = ValidParenthesesSolution()

  def test_valid_parentheses_true(self):
    s = "()[]{}"
    assert self.solution.isValid(s) == True

  def test_valid_parentheses_false(self):
    s = "([)]"
    assert self.solution.isValid(s) == False

  def test_valid_parentheses_nested(self):
    s = "{[()]}"
    assert self.solution.isValid(s) == True

  def test_valid_parentheses_empty(self):
    s = ""
    assert self.solution.isValid(s) == False

  def test_valid_parentheses_single(self):
    s = "("
    assert self.solution.isValid(s) == False


class TestMinimumStack:

  def test_minimum_stack_operations(self):
    # Test the MinStack class directly
    min_stack = MinimumStackSolution()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2

  def test_minimum_stack_single_element(self):
    min_stack = MinimumStackSolution()
    min_stack.push(5)
    assert min_stack.top() == 5
    assert min_stack.getMin() == 5

  def test_minimum_stack_duplicate_min(self):
    min_stack = MinimumStackSolution()
    min_stack.push(1)
    min_stack.push(2)
    min_stack.push(1)
    assert min_stack.getMin() == 1
    min_stack.pop()
    assert min_stack.getMin() == 1


class TestEvaluateReversePolishNotation:

  def setup_method(self):
    self.solution = EvaluateReversePolishNotationSolution()

  def test_evaluate_rpn_basic(self):
    tokens = ["2", "1", "+", "3", "*"]
    result = self.solution.evalRPN(tokens)
    assert result == 9

  def test_evaluate_rpn_complex(self):
    tokens = ["4", "13", "5", "/", "+"]
    result = self.solution.evalRPN(tokens)
    assert result == 6

  def test_evaluate_rpn_negative(self):
    tokens = [
        "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"
    ]
    result = self.solution.evalRPN(tokens)
    assert result == 22


class TestGenerateParentheses:

  def setup_method(self):
    self.solution = GenerateParenthesesSolution()

  def test_generate_parentheses_n1(self):
    n = 1
    result = self.solution.generateParenthesis(n)
    assert sorted(result) == ["()"]

  def test_generate_parentheses_n2(self):
    n = 2
    result = self.solution.generateParenthesis(n)
    expected = ["(())", "()()"]
    assert sorted(result) == sorted(expected)

  def test_generate_parentheses_n3(self):
    n = 3
    result = self.solution.generateParenthesis(n)
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sorted(result) == sorted(expected)


class TestDailyTemperatures:

  def setup_method(self):
    self.solution = DailyTemperaturesSolution()

  def test_daily_temperatures_basic(self):
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    result = self.solution.dailyTemperatures(temperatures)
    expected = [1, 1, 4, 2, 1, 1, 0, 0]
    assert result == expected

  def test_daily_temperatures_ascending(self):
    temperatures = [30, 40, 50, 60]
    result = self.solution.dailyTemperatures(temperatures)
    expected = [1, 1, 1, 0]
    assert result == expected

  def test_daily_temperatures_descending(self):
    temperatures = [30, 60, 90]
    result = self.solution.dailyTemperatures(temperatures)
    expected = [1, 1, 0]
    assert result == expected


class TestCarFleet:

  def setup_method(self):
    self.solution = CarFleetSolution()

  def test_car_fleet_basic(self):
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    result = self.solution.carFleet(target, position, speed)
    assert result == 3

  def test_car_fleet_single_car(self):
    target = 10
    position = [3]
    speed = [3]
    result = self.solution.carFleet(target, position, speed)
    assert result == 1

  def test_car_fleet_no_cars(self):
    target = 10
    position = []
    speed = []
    result = self.solution.carFleet(target, position, speed)
    assert result == 0


class TestLargestRectangleInHistogram:

  def setup_method(self):
    self.solution = LargestRectangleInHistogramSolution()

  def test_largest_rectangle_basic(self):
    heights = [2, 1, 5, 6, 2, 3]
    result = self.solution.largestRectangleArea(heights)
    assert result == 10

  def test_largest_rectangle_single(self):
    heights = [2]
    result = self.solution.largestRectangleArea(heights)
    assert result == 2

  def test_largest_rectangle_ascending(self):
    heights = [1, 2, 3, 4, 5]
    result = self.solution.largestRectangleArea(heights)
    assert result == 9

  def test_largest_rectangle_same_height(self):
    heights = [3, 3, 3, 3]
    result = self.solution.largestRectangleArea(heights)
    assert result == 12
