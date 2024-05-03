class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans = 0
        for i in range(len(s)):
            current = dict[s[i]]
            next = dict[s[i+1]] if i+1 < len(s) else 0
            if current < next:
                ans -= current
            else:
                ans += current
        return ans

#s = "MCMXCIV"
s = "MCMXCIV"
solution = Solution()
print(solution.romanToInt(s))