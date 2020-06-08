class Solution(object):
    # Explanation - https://leetcode.com/problems/power-of-two/solution/
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (-n) == n

s = Solution()
ans = s.isPowerOfTwo(7)
print(ans)