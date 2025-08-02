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

  def groupAnagramsDict(self, strs: list[list]) -> list[list[str]]:
    resultArray = []

    sameDict = collections.defaultdict(list)
    for index in strs:
      SortedResult = sorted(index)
      keyString = ''.join(SortedResult)
      sameDict[keyString].append(index)

    for keys, values in sameDict.items():
      resultArray.append(values)
    return resultArray


if __name__ == "__main__":
  Testcase = Solution()

  strs1 = ["act", "pots", "tops", "cat", "stop", "hat"]
  strs2 = ["x"]

  results1 = Testcase.groupAnagrams(strs1)
  resultsDict = Testcase.groupAnagramsDict(strs1)
  print(results1)
  print(resultsDict)

  results2 = Testcase.groupAnagrams(strs2)
  print(results2)
"""
解法和上一个类似, 通过走一个循环的方式来找出字符数量和类型相同的字符, 只不过这次是塞进一个新的array。整个anagram的核心就在

count = [0] * 26
count[ord(c) - ord('a)] += 1

不管是之前的对比也好还是现在的集合也好, 核心都是去找字符数量和类型相同的
"""
