class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n , cnt = x ^ y , 0
        while n :
            n = n & (n-1)
            cnt += 1
        return cnt

    def hammingDistance1(self, x: int, y: int) -> int:
        ans = x ^ y
        s = bin(ans)[2:]
        return sum(1 for x in s if x == '1')


s = Solution()
ip = []
ans = s.hammingDistance(1,4)
print(ans)