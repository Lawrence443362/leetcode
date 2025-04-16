# Two sums
class Solution(object):
    def twoSum(self, numbers, target):
        array_range = range(len(numbers))

        for i in array_range:
            for j in array_range:
                if (numbers[i] + numbers[j]) == target and i != j: 
                    return [i + 1, j + 1] 