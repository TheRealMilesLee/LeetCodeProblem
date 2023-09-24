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
    /**
     * @brief Go through the string, find each letter appear time and record with its
     * position by using this word to subtract ASCII first letter 'a'. charCount[characterIterate - 'a']++ means
     * at position of that character, that character appear once.
     * @param word is the string input
     */
    for (char& characterIterate : word)
    {
      charCount[characterIterate - 'a']++;
    }
    for (size_t index = 0; index < 26; index++)
    {
      // Border judge, if the first index is 0, then skip this iteration
      if (charCount[index] == 0)
      {
        continue;
      }
      /* Check if deleting a character from the word will result in all
      remaining characters having the same frequency. */
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
