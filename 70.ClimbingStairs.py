class Solution:
    def climbStairs(self, n: int) -> int:
        """Fibonacci sequence"""
        aux1, aux2 = 1, 1 #first and second term of fibonacci sequence

        if n <= 1:
            return n
        
        for _ in range(2, n+1):  
            ways = aux1 + aux2
            aux1 = aux2
            aux2 = ways
        return ways


a = 5
solution = Solution()
print(solution.climbStairs(a))
