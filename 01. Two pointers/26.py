# Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0

        for fast in range(len(nums)): 
            tmp_slow = nums[slow]
            tmp_fast = nums[fast]

            if tmp_slow != tmp_fast:
                slow += 1
                nums[slow] = tmp_fast
            
            tmp_fast += 1

        return slow + 1
            
