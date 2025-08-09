"""
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.
"""


class Solution:

  def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
      return False

    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
      s1Count[ord(s1[i]) - ord('a')] += 1
      s2Count[ord(s2[i]) - ord('a')] += 1

    matches = 0
    for i in range(26):
      matches += (1 if s1Count[i] == s2Count[i] else 0)

    l = 0
    for r in range(len(s1), len(s2)):
      if matches == 26:
        return True

      index = ord(s2[r]) - ord('a')
      s2Count[index] += 1
      if s1Count[index] == s2Count[index]:
        matches += 1
      elif s1Count[index] + 1 == s2Count[index]:
        matches -= 1

      index = ord(s2[l]) - ord('a')
      s2Count[index] -= 1
      if s1Count[index] == s2Count[index]:
        matches += 1
      elif s1Count[index] - 1 == s2Count[index]:
        matches -= 1
      l += 1
    return matches == 26


if __name__ == '__main__':
  TestCase = Solution()
  string1 = "ab"
  string2 = "lecabee"
  Result1 = TestCase.checkInclusion(string1, string2)
  print(Result1)

"""
在s2上滑动一个大小为len(s1)的窗口, 然后看窗口内的字符串是否和s1匹配

因为要考虑到可能排列顺序不一样, 所以需要像之前一样维护一个array, 如果这俩一样的话array的每一个元素都应该是0, 否则就是不一样(长度为26, s1是加s2是减)
"""
