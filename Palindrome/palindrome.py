class Palindrome:

  def isPalindrome(self, inputString: str, compareString: str) -> bool:
    checkIfExist = []
    index = 0

    while index < len(compareString):
      checkIfExist.append(compareString[index])
      index += 1

    reverseIndex = len(inputString) - 1
    index = 0

    while reverseIndex >= 0:
      if inputString[reverseIndex] != checkIfExist[index]:
        return False
      reverseIndex -= 1
      index += 1

    return True


if __name__ == '__main__':
  p = Palindrome()
  print(p.isPalindrome('amanaplanacanalpanama', 'amanaplanacanalpanama'))
  print(p.isPalindrome('asandaman', 'amanaplanacanalpanama'))
