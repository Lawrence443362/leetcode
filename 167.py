# 167. Two Sum II - Input Array Is Sorted
class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            summ = numbers[left] + numbers[right]
            
            if summ == target and left != right:
                return [left + 1, right + 1]
            elif target < summ: 
                right -= 1
            elif target > summ:
                left += 1
            else:
                break