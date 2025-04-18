# 1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        len1, len2 = len(word1), len(word2)
        result = ""
        
        while i < max(len1, len2):
            if i < len1:
                result += word1[i]

            if i < len2:
                result += word2[i]

            i += 1

        return result