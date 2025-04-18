# Is Subsequence
class Solution:
    def isSubsequence(self, substring: str, target: str) -> bool:
        left = len(substring) - 1
        right = len(target) - 1

        while right >= 0:
            if left == -1: 
                break

            if substring[left] == target[right]:
                left -= 1

            right -= 1

        return left == -1
            
            
