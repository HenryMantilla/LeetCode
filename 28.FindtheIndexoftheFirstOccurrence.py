class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lh, ln = len(haystack), len(needle)
        if not needle:
            return 0
        if lh<ln:
            return -1
        for i in range(lh-ln+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1    

haystack, needle = "sadbutsad", "sad"
solution = Solution()
print(solution.strStr(haystack, needle))