from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str, max_str = min(strs), max(strs)
        for i in range(len(min_str)):
            if min_str[i] != max_str[i]:
                return min_str[:i]
        return min_str
    
s = ["aaa","aa","aaa"]
solution = Solution()
print(solution.longestCommonPrefix(s))