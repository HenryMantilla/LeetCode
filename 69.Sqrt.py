class Solution:
    def mySqrt(self, x: int) -> int:
        MIN, MAX = 0, x
        sqrt = (MIN+MAX)/2

        if x < 2:
            return x
        
        while abs(sqrt**2 - x) > 1e-5:
            if sqrt**2 > x:
                MAX = sqrt
            else:
                MIN = sqrt
            sqrt = (MIN+MAX)/2

        return int(sqrt)
            

a = 1
solution = Solution()
print(solution.mySqrt(a))