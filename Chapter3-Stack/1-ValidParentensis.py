"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.
"""


class Solution:

  def isValid(self, s: str) -> bool:
    stack = []

    openParent = ["{", "[", "("]
    for index in s:
      if index in openParent:
        stack.append(index)
      else:
        if len(stack) == 0:
          return False

        if (index == ")" and stack[len(stack) - 1]
            == "(") or (index == "}" and stack[len(stack) - 1] == "{") or (
                index == "]" and stack[len(stack) - 1] == "["):
          stack.pop()
        else:
          return False

      if stack == []:
        return True
    return False


if __name__ == "__main__":
  TestCase = Solution()
  Result1 = TestCase.isValid("[]")
  print(Result1)

  TestCase = Solution()
  Result2 = TestCase.isValid("([{}])")
  print(Result2)

  TestCase = Solution()
  Result3 = TestCase.isValid("]")
  print(Result3)

  TestCase = Solution()
  Result4 = TestCase.isValid("(])")
  print(Result4)
