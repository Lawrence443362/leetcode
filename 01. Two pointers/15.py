# 15. 3Sum
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = set()
        n = len(nums)
        
        for i in range(n):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else: 
                    right -= 1

        return list(result)