class Solution:
    def addBinary(self, a: str, b: str) -> str:
        add = bin(int(a,2)+ int(b,2))
        return add[2:]
    
a = "11"
b = "1"
solution = Solution()
print(solution.addBinary(a,b))