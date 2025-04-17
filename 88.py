class Solution(object):
    def merge(self, nums1, m, nums2, n):
        left = 0
        right = 0

        left_list = nums1[:m] 
        right_list = nums2[:n]

        result = []

        while left < len(left_list) and right < len(right_list):
            if left_list[left] < right_list[right]:
                result.append(left_list[left])
                left += 1
            else:
                result.append(right_list[right])
                right += 1

        result.extend(left_list[left:m])
        result.extend(right_list[right:n])

        return result

        