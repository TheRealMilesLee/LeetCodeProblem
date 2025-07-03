"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different
"""
import collections


def solution(string1: str, string2: str) -> bool:
  myDict = collections.defaultdict()
  for index in string1:
    if index in myDict:
      myDict[index.lower()] += 1
    else:
      myDict[index.lower()] = 1

  myDict2 = collections.defaultdict()
  for index2 in string2:
    if index2 in myDict2:
      myDict2[index2.lower()] += 1
    else:
      myDict2[index2.lower()] = 1

  if myDict2 == myDict:
    return True
  return False


if __name__ == "__main__":
  string1 = "racecar"
  string2 = "carrace"
  results1 = solution(string1, string2)
  print(results1)

  string3 = "jar"
  string4 = "jam"
  results2 = solution(string3, string4)
  print(results2)
