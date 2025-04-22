# 15. 3Sum
class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        result = []
        nums_len = len(nums)
        
        for i in range(nums_len):
            left = i + 1
            right = nums_len - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Пропускаем одинаковые i

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                print("{}, {}, {} = {}".format(nums[i], nums[left], nums[right], sum))

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    if i != left and i != right and left != right:
                        result.append([nums[i], nums[left], nums[right]])
                        
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1


        return result
        