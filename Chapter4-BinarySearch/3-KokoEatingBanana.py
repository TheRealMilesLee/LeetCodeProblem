"""
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.
"""
import math


class Solution:

  def minEatingSpeed(self, piles: list[int], h: int) -> int:
    left = 1
    right = max(piles)

    results = right

    while left <= right:
      k = (left + right) // 2

      totalTime = 0
      for index in piles:
        totalTime += math.ceil(float(index) / k)
      if totalTime <= h:
        results = k
        right = k - 1
      else:
        left = k + 1
    return results


if __name__ == '__main__':
  TestCase = Solution()

  piles = [1, 4, 3, 2]
  Result1 = TestCase.minEatingSpeed(piles, 9)
  print(Result1)
"""
trickey 的地方主要是找最小的rate. 我们知道最大的rate可以直接通过找当前array的最大值获得, 但是要找最小的rate并且要保证吃完, 核心思路还是先找到最大的然后逐步递减看还能不能吃完, 所以brute force的做法就是一个一个倒着尝试

BUT WE CAN DO BETTER, 从大的往小的尝试我们也可以用二分法来加速这个过程, 前面过程都一样, 找到最大的piles以后根据最大的pile生成一个从1到这个数字的array, 然后left是1, right是这个大数, middle就是(left + right) / 2, 如果发现middle还能完成,则right = middle, 如果middle不能完成, 则left = middle
"""
