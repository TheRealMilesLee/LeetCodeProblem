"""
Given a string s, return true if it is a palindrome, otherwise return false

A palindrome is a string that reads the same forward and backward. It is also case insensitive and ignores all non-alphanumeric character
"""


class Solution:

  def isPalindrome(self, s: str) -> bool:
    toloweredString = s.lower()
    filteredString = ""
    for index in toloweredString:
      if index.isalpha() or index.isnumeric():
        filteredString += index

    ptrStart = 0
    ptrEnd = len(filteredString) - 1
    while ptrStart < len(filteredString) and ptrEnd > 0:
      if filteredString[ptrStart] != filteredString[ptrEnd]:
        return False
      ptrStart += 1
      ptrEnd -= 1
    return True


if __name__ == "__main__":
  TestCase = Solution()

  string1 = "Was it a car or a cat I saw?"
  Result1 = TestCase.isPalindrome(string1)
  print(Result1)

  string2 = "tab a cat"
  Result2 = TestCase.isPalindrome(string2)
  print(Result2)
"""
经典双指针, 需要注意的点就是要统一大小写, 并且要筛掉非数字和字母的字符. 然后剩下的就是简单的一头一尾两个指针向中间走就好了
"""
