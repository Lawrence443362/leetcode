# 16. 3Sum Closest
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        n = len(nums)

        for i in range(n):
            left, right = i + 1, n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == target:
                    return target
                elif s < target:
                    result = self.choose_closest(result, s, target)
                    left += 1
                else:
                    result = self.choose_closest(result, s, target)
                    right -= 1

        return result
    
    def choose_closest(self, prev, current, target):
        if abs(prev - target) < abs(current - target):
            return prev
        else:
            return current