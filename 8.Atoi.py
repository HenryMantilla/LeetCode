class Solution:
    def myAtoi(self, s: str) -> int:
        MIN, MAX = -2**31, 2**31-1
        ans = ''
        s = s.strip()
        if not s:
            return 0
        sign = -1 if len(s)>1 and s[0]=='-' else 1
        if s[0] in {'-','+'}:
            s = s[1:]
        for char in s:
            if not char.isdigit():
                break
            ans += char
        if len(ans) == 0:
            return 0
        if sign * int(ans) < MIN:
            return MIN
        elif sign * int(ans) > MAX:
            return MAX
        else:
            return sign * int(ans) 

    
s = "words and 987"
s1 = "42"
s2 = "-91283472332"
solution = Solution()
print(solution.myAtoi(s))