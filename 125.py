class Solution(object):
    def isPalindrome(self, string):
        string = string.lower()
        only_letters = (c for c in string if c.isalnum())
        result = "".join(only_letters)

        print(result)
        return result == "".join(reversed(result))        