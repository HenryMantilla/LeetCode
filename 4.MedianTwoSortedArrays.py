from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        full_array = nums1 + nums2
        full_array.sort()
        arr_len = len(full_array)
        if arr_len % 2 == 0:
            mean_idx = int(arr_len / 2)
            return (full_array[mean_idx]+full_array[mean_idx-1])/2
        else:
            mean_idx = -(-len(full_array) // 2)
            return float(full_array[mean_idx-1])

nums1 = [1,3]
nums2 = [2]
solution = Solution()
solution.findMedianSortedArrays(nums1, nums2)