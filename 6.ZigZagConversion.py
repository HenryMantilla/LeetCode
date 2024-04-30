class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = [""] * numRows
        row_idx = 0
        aux = (numRows==1)-1

        for char in s:
            zigzag[row_idx] += char
            if row_idx == numRows-1 or row_idx == 0:
                aux *= -1
            row_idx += aux
        ans = ''.join(zigzag)
        print(ans)
        return ans

s = "PAYPALISHIRING"
solution = Solution()
solution.convert(s, 3)