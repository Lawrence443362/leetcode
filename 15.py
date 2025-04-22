# 15. 3Sum
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = set()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break  # Все числа после будут положительными

            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Пропускаем дубликаты

            left, right = i + 1, len(nums) - 1
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