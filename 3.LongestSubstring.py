import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        aux, ans = 0, 0
        count = collections.Counter()
        for idx, char in enumerate(s):
            count[char] += 1
            while count[char] > 1:
                count[s[aux]] -= 1
                aux += 1
            ans = max(ans, idx - aux + 1)
        return ans
    
s1 = "abcabcbb"
s2 = "bbbbbbbb"
s3 = "pwwkew"
solution = Solution()
solution.lengthOfLongestSubstring(s3)
