# 5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        result = ""
        for left in range(len(s)):
            right = n - 1

            while left <= right:
                if s[left] == s[right]:
                    if self.isPalindrome(s, left, right):
                        result = self.chooseLongestString(result, s[left:right+1])
                        break
                right -= 1

        return result

    def isPalindrome(self, s, left, right): 
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1

                continue
            else:
                return False
        
        return True
    
    def chooseLongestString(self, s1, s2): 
        if len(s1) > len(s2):
            return s1
        else:
            return s2