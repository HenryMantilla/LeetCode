class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = s.strip().split(" ")
        return len(last[-1])

s = "   fly me   to   the moon  " 
solution = Solution()
print(solution.lengthOfLastWord(s))