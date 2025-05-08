# 496. Next Greater Element I
class Solution:
    def nextGreaterElement(self, sub_nums, nums):
        stack = []
        for n in sub_nums:
            next = self.getNextValue(nums, n)
            if next and n < next:
                stack.append(next)
            else: 
                stack.append(-1)

        return stack
           
    def getNextValue(self, nums, value):
        i = self.getCurrentIndex(nums, value)

        while i < len(nums):
           if nums[i] > value:
               return nums[i]

           i += 1 

    def getCurrentIndex(self, nums, value):
        for i in range(len(nums)):
            if nums[i] == value: 
                return i