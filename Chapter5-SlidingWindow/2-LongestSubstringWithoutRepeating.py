"""
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.
"""
import collections


class Solution:

  def lengthOfLongestSubstring(self, s: str) -> int:
    saveDict = collections.defaultdict()
    left = 0
    results = 0

    index = 0

    while index < len(s):
      if s[index] in saveDict:
        left = max(saveDict[s[index]] + 1, left)
      saveDict[s[index]] = index
      results = max(results, index - left + 1)
      index += 1
    return results


if __name__ == '__main__':
  TestCase = Solution()
  s1 = "abcabcbb"
  Result1 = TestCase.lengthOfLongestSubstring(s1)
  print(Result1)
"""
字节考过, 核心思想是用左右两个指针来表示当前不重复的substring长度, 默认right向右边走, 同时用dict来记录每一个字符出现的对应index, 如果遇到重复的, 则把left移动到重复字符的下一个, 然后最后用right - left + 1来获取最大长度
"""
