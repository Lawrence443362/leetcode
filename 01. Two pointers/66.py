# 66. Plus One

class Solution:
    def plusOne(self, digits):
        index = len(digits) - 1

        while index != -2:
            if index == -1:
                digits = [1] + digits
                break
            if digits[index] + 1 == 10:
                digits[index] = 0
                index -= 1
            else:
                digits[index] += 1
                break
        
        print(digits)