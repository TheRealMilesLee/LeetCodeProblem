"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different
"""
class Solution:

  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    count = [0] * 26
    for i in range(len(s)):
      count[ord(s[i]) - ord('a')] += 1
      count[ord(t[i]) - ord('a')] -= 1

    for val in count:
      if val != 0:
        return False
    return True


if __name__ == "__main__":
  TestCase = Solution()
  string1 = "racecar"
  string2 = "carrace"
  results1 = TestCase.isAnagram(string1, string2)
  print(results1)

  string3 = "jar"
  string4 = "jam"
  results2 = TestCase.isAnagram(string3, string4)
  print(results2)

"""
注意读题, 这个地方的anagram是指的是两个字符串所包含的字母相同, 字符数量也相同.

我们可以用一个array来记录中间的区别, 对于第一个string来说, 出现了一个字母，我们就在这个字母上 + 1, 如果这个字母在第二个string中也出现了,则在相同的地方进行 - 1, 那么这样下来如果两个字符串使用的字母相同, 字符数量也相同的话, 最后的array应该全是0, 只要有一项不相同, 则在array中就一定会出现一个位置是不为0的
"""
