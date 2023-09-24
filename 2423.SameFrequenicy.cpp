/*
 * @lc app=leetcode.cn id=2423 lang=cpp
 *
 * [2423] 删除字符使频率相同
 */
#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <unordered_set>

using namespace std;

class Solution
{
public:
  bool equalFrequency(string word)
  {
    int charCount[26] = {0};
/* This code snippet is iterating over each character `c` in the string `word` and incrementing the
count of that character in the `charCount` array. The expression `c - 'a'` is used to convert the
character `c` to an index in the `charCount` array. Since the characters in `word` are assumed to be
lowercase letters, subtracting `'a'` from `c` gives the index of the character in the range of 0 to
25 (corresponding to the letters 'a' to 'z'). */
    for (char& characterIterate : word)
    {
      charCount[characterIterate - 'a']++;
    }
    /* This code snippet is iterating over each index `index` in the `charCount` array. If the count of
    the character at that index is 0, it continues to the next iteration. Otherwise, it decrements
    the count of that character by 1 and creates an unordered set `frequency` to store the
    frequencies of the remaining characters. */
    for (size_t index = 0; index < 26; index++)
    {
      if (charCount[index] == 0)
      {
        continue;
      }
      charCount[index]--;
      unordered_set<int> frequency;
      for (int frequent : charCount)
      {
        if (frequent > 0)
        {
          frequency.insert(frequent);
        }
      }
      if (frequency.size() == 1)
      {
        return true;
      }
      charCount[index]++;
    }
    return false;
  }
};
// @lc code=end
