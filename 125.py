# Valid Palindrome
class Solution(object):
    def isPalindrome(self, string):
        string = string.lower()
        left, right = 0, len(string) - 1

        while left < right:
            if string[left].isalnum() and string[right].isalnum():
                if string[left] != string[right]:
                    return False
                else:
                    left += 1
                    right -= 1

            if string[left].isalnum() == False:
                left += 1

            if string[right].isalnum() == False:
                right -= 1

        return True