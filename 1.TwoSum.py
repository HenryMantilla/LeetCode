from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = {}
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in dictionary:
                return [dictionary[comp], idx]
            dictionary[num] = idx
        return []