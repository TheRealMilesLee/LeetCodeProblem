"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings
"""


class Solution:

  def encode(self, strs: list[str]) -> str:
    resultString = ""
    for index in strs:
      resultString += str(len(index)) + "$" + index
    return resultString

  def decode(self, s: str) -> list[str]:
    resultString = []
    index = 0

    while index < len(s):
      checkCurrentIndex = index
      while s[checkCurrentIndex] != "$":
        checkCurrentIndex += 1
      length = int(s[index:checkCurrentIndex])
      index = checkCurrentIndex + 1
      checkCurrentIndex = index + length
      resultString.append(s[index:checkCurrentIndex])
      index = checkCurrentIndex

    return resultString


if __name__ == "__main__":
  TestCase = Solution()

  string1 = ["neet", "code", "love", "you"]
  encodeResult1 = TestCase.encode(string1)
  decodeResult1 = TestCase.decode(encodeResult1)
  print(
      f"Original: {string1}, Encode: {encodeResult1}, Decode: {decodeResult1}"
  )

"""
实际上tricky part在如何去找分隔符来体现当前这个string和下一个string, 因为要求是stateless的, 所以最佳的解法就是在每个string前面加上当前string的长度和一个符号代表起点, 就像这样:

4#abcd

在这个例子中, 4就是abcd字符串的长度, #就是代表起点部分. 然后在解码部分就直接按着这个拆就完事
"""
