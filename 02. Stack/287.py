# 287. Find the Duplicate Number
class Solution:
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[0]

        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        
        
