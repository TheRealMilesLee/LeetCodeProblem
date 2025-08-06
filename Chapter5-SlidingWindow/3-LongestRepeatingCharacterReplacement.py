"""
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
"""

import collections


class Solution:

  def characterReplacement(self, s: str, k: int) -> int:
    count = collections.defaultdict()
    results = 0

    left = 0
    maxLength = 0

    for right in range(len(s)):
      count[s[right]] = 1 + count.get(s[right], 0)
      maxLength = max(maxLength, count[s[right]])

      while (right - left + 1) - maxLength > k:
        count[s[left]] -= 1
        left += 1
      results = max(results, right - left + 1)
    return results


if __name__ == '__main__':
  TestCase = Solution()
  string1 = "XYYX"
  Result1 = TestCase.characterReplacement(string1, 2)
  print(Result1)
