"""
Given an integer arry nums and an integer k, return the k most frequent elements within the array

The test cases are generated such that the answer is always unique, you may return the output in any order
"""


class Solution:

  def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
      count[num] = 1 + count.get(num, 0)
    for num, cnt in count.items():
      freq[cnt].append(num)

    res = []
    for i in range(len(freq) - 1, 0, -1):
      for num in freq[i]:
        res.append(num)
        if len(res) == k:
          return res


if __name__ == "__main__":
  TestCase = Solution()

  nums1 = [1, 2, 2, 3, 3, 3]
  k = 2
  result1 = TestCase.topKFrequent(nums1, k)
  print(result1)

  nums2 = [-1, 2]
  k = 1
  result2 = TestCase.topKFrequent(nums2, k)
  print(result2)
"""
用Key来表示出现的次数, 用 [Values] 来表示这个数字, 比如[1,1,1,2,2,100], 表如下

i (count) | 0 |   1   |  2  |  3  | 4 | 5 | 6 |
-----------------------------------------------
values    |   | [100] | [2] | [1] |   |   |   |

然后最后要找的是top k, 于是只需要输出有values的top k个就好 (比如top 2就直接输出 count 3对应的values, 也就是1, 和 count 2对应的values, 也就是2)
"""
