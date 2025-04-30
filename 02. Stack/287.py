# 287. Find the Duplicate Number
class Solution:
    def findDuplicate(self, nums):
        nums.sort()
        slow, fast = 0, 1
        n = len(nums)

        while fast < n:
            if nums[slow] == nums[fast]:
                return nums[fast]
            else:
                slow += 1
                fast += 1