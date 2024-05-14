from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                idx += 1
                nums[idx] = nums[i]
        return idx

s = [1,1,2]
solution = Solution()
print(solution.removeDuplicates(s))