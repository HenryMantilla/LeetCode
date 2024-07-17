from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height)-1

        while left < right:
            min_pointer = min(height[left], height[right])
            max_area = max(max_area, min_pointer * (right-left))

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return max_area


height = [1,1]
solution = Solution()
print(solution.maxArea(height))