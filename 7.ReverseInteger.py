class Solution:
    def reverse(self, x: int) -> int:
        reversed = int(str(abs(x))[::-1])
        ans = -reversed if x < 0 else reversed
        return ans if reversed.bit_length() < 32 else 0

s = -123
solution = Solution()
print(solution.reverse(s))