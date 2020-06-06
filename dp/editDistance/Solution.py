from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dist(m,n) :
            if m < 0 or n < 0 : return abs(m-n)
            if word1[m] == word2[n] :
                return dist(m-1,n-1)
            else:
                return min(dist(m-1,n), dist(m,n-1), dist(m-1,n-1)) +1 # delete, insert, replace
        return dist(len(word1)-1,len(word2)-1)

    def minDistanceDP(self, word1: str, word2: str) -> int:
        m ,n = len(word1)+1 , len(word2)+1
        dp = [ [0] * n  for _ in range(m)]
        for i in range(m):
            dp[i][0] = i
        for j in range(n):
            dp[0][j] = j

        for i in range(1,m) :
            for j in range(1,n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else :
                    dp[i][j] = 1 + min( dp[i-1][j] ,
                                        dp[i][j-1],
                                        dp[i-1][j-1]) 
        # print(dp)
        return dp[m-1][n-1]


s = Solution()
# ans = s.minDistance('intention','execution')
# print(ans)

ans = s.minDistanceDP('intention','execution')
print(ans)