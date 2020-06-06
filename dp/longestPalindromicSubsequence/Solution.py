from functools import lru_cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def helper(b,e):
            print(b,e)
            if b > e : return 0
            if b == e : return 1
            if s[b] == s[e] : 
                return helper(b+1,e-1) + 2
            return max(helper(b+1,e), helper(b,e-1))
        return helper(0,len(s)-1)


s = Solution()
ans = s.longestPalindromeSubseq('bcbbd')
print(ans)