class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 : return s
        res = [''] *numRows
        r , d = 0 , -1
        for c in s:
            res[r] += c
            # print(res)
            if r == numRows -1 or r == 0:
                d = -1 * d
            r += d
        return ''.join(res)


s = Solution()
print(s.convert('PAYPALISHIRING',4))