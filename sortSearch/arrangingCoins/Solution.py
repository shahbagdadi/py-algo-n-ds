class Solution:
    def arrangeCoins(self, n: int) -> int:
        l , r = 0, n
        while l <= r :
            m = (l+r) //2
            cur = m * (m+1) //2
            if cur == n :
                return m
            elif cur < n :
                l = m +1
            else:
                r = m -1
        return r

s = Solution()
ip = []
ans = s.arrangeCoins(5)
print(ans)
