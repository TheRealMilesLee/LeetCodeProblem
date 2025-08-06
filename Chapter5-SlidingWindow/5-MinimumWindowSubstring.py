"""
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.
"""


class Solution:

  def minWindow(self, s: str, t: str) -> str:
    if t == "":
      return ""

    countT, window = {}, {}
    for c in t:
      countT[c] = 1 + countT.get(c, 0)

    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("infinity")
    l = 0
    for r in range(len(s)):
      c = s[r]
      window[c] = 1 + window.get(c, 0)

      if c in countT and window[c] == countT[c]:
        have += 1

      while have == need:
        if (r - l + 1) < resLen:
          res = [l, r]
          resLen = r - l + 1

        window[s[l]] -= 1
        if s[l] in countT and window[s[l]] < countT[s[l]]:
          have -= 1
        l += 1
    l, r = res
    return s[l:r + 1] if resLen != float("infinity") else ""


if __name__ == '__main__':
  TestCase = Solution()
  string1 = "ADOBECODEBANC"
  string2 = "ABC"
  Result1 = TestCase.minWindow(string1, string2)
  print(Result1)
