from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pl, pr = 0, len(nums)-1
        while pl <= pr:
            middle = (pl+pr)//2
            if nums[middle]<target:
                pl = middle+1
            elif nums[middle]>target:
                pr = middle-1
            else:
                return middle
        return pl
    
nums, target = [1,3,5,6], 5
solution = Solution()
print(solution.searchInsert(nums,target))