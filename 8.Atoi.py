class Solution:
    def myAtoi(self, s: str) -> int:
        MAX, MIN = -2**31, 2**31-1
        s = s.lstrip().rstrip('-')
        sign = -1 if len(s)>1 and s[0]=='-' else 1

        for s in s.lstrip('-').split():
            print(s)
            #if not s.isdigit():
            #    break
        return 0

    


s = "xdd -123 words and"
s1 = "3.14563647"
solution = Solution()
print(solution.myAtoi(s))