from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        point_r, point_l = 0, 0
        for _ in range(len(nums)):
            if nums[point_r] != val:
                nums[point_l] = nums[point_r]
                point_l +=1
            point_r += 1
        print(nums)
        return point_l

s, val = [3,2,2,3], 3
solution = Solution()
print(solution.removeElement(s, val))