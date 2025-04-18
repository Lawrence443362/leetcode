# 1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        word1_len = len(word1)
        word2_len = len(word2)
        max_len = max(word1_len, word2_len)

        if word2_len > word1_len:
            for i in range(max_len):
                if i < word1_len:
                    result += word1[i] + word2[i]
                else:
                    result += word2[i]
        else:
            for i in range(max_len):
                if i < word2_len:
                    result += word1[i] + word2[i]
                else:
                    result += word1[i]
        
        return result