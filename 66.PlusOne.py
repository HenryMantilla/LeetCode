from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lst2str = ''.join(str(x) for x in digits)
        tmp = int(lst2str)+1
        return [int(i) for i in str(tmp)]

s = [1,2,3] 
solution = Solution()
print(solution.plusOne(s))