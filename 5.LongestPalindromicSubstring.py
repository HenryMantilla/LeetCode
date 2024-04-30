class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            tmp = expand(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = expand(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res
    
def expand(s, left, right):
    length = len(s)
    while left >= 0 and right < length and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1 : right]

s = "babad"
solution = Solution()
solution.longestPalindrome(s)