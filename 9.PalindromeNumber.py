class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x) 

s = 10
solution = Solution()
print(solution.isPalindrome(s))