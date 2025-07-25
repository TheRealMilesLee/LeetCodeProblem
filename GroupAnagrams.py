"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""
import collections


class Solution:

  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    results = collections.defaultdict(list)
    for strsIndex in strs:
      count = [0] * 26
      for countIndex in strsIndex:
        count[ord(countIndex) - ord('a')] += 1
      results[tuple(count)].append(strsIndex)
    return list(results.values())


if __name__ == "__main__":
  Testcase = Solution()

  strs1 = ["act", "pots", "tops", "cat", "stop", "hat"]
  strs2 = ["x"]

  results1 = Testcase.groupAnagrams(strs1)
  print(results1)

  results2 = Testcase.groupAnagrams(strs2)
  print(results2)
