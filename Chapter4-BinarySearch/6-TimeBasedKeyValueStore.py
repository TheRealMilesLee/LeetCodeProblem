"""
Implement a time-based key-value data structure that supports:

    Storing multiple values for the same key at specified time stamps
    Retrieving the key's value at a specified timestamp

Implement the TimeMap class:

    TimeMap() Initializes the object.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".

Note: For all calls to set, the timestamps are in strictly increasing order.
"""
import collections


class TimeMap:

  def __init__(self):
    self.TimeMapStore = collections.defaultdict(list)

  def set(self, key: str, value: str, timestamp: int) -> None:
    self.TimeMapStore[key].append([value, timestamp])

  def get(self, key: str, timestamp: int) -> str:
    results = ""
    values = self.TimeMapStore.get(key, [])
    left = 0
    right = len(values) - 1

    while left <= right:
      middle = (left + right) // 2

      if values[middle][1] <= timestamp:
        results = values[middle][0]
        left = middle + 1
      else:
        right = middle - 1
    return results


if __name__ == '__main__':
  timeMap = TimeMap()

  timeMap.set("alice", "happy", 1)
  # store the key "alice" and value "happy" along with timestamp = 1.
  checkPoint = timeMap.get("alice", 1)
  # return "happy"
  checkPoint2 = timeMap.get("alice", 2)
  # return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
  timeMap.set("alice", "sad", 3)
  # store the key "alice" and value "sad" along with timestamp = 3.
  checkPoint3 = timeMap.get("alice", 3)
  # return "sad"

  print(checkPoint)
  print(checkPoint2)
  print(checkPoint3)


"""
我们可以用dict来存储key value之间的关系, 然后至于timestamp的问题, value我们可以存为list, 因为说了timestamp are in strict increasing order, 所以可以用二分查找来定位timestamp所对应的value(也就是array的index[0])

有一个知识点要注意, 就是dictionary的get()方法, 这个可以针对性的get当前key所对应的value
"""
