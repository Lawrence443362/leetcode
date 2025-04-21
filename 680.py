# 680. Valid Palindrome II
class Solution:
    def validPalindrome(self, string: str) -> bool:     
        left, right = 0, len(string) - 1

        while left < right:
            if string[left] != string[right]:
                return self.isPalindrome(string, left + 1, right) or self.isPalindrome(string, left, right - 1)
            
            left += 1
            right -= 1

        return True

    def isPalindrome(self, string, left, right): 
        while left < right:
            if string[left] != string[right]:
                return False
            
            left += 1
            right -= 1

        return True
