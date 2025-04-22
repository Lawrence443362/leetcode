# 557. Reverse Words in a String III
class Solution:
    def reverseWords(self, string: str) -> str:
        items = string.split(" ")
        
        for i in range(len(items)):
            items[i] = self.reverseSingleWord(items[i])

        return " ".join(items)


    def reverseSingleWord(self, string):
        left, right = 0, len(string) - 1
        letters = list(string)

        while left < right:
            letters[left], letters[right] = letters[right], letters[left]
            left += 1
            right -= 1

        return "".join(letters)