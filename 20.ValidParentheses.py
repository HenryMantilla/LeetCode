import time
class Solution:
    def isValid(self, s: str) -> bool:
        open_br = ['(', '{', '[']
        close_br = [')', '}', ']']
        map = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for i in range(len(s)):
            if s[i] in open_br:
                stack.append(s[i])
            elif s[i] in close_br:
                if not stack or stack.pop() != map[s[i]]:
                    return False
                else:
                    continue
        return stack == []

s = ["[", "{[]}","(]", "(){}}{", "()[]{}"]
solution = Solution()
for sol in s:
   print(solution.isValid(sol))
