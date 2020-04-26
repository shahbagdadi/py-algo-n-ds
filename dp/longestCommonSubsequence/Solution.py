class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M,N=len(text1),len(text2)
        dp=[[0]*(N+1) for _ in range(M+1)]
        for m in range(M):
            for n  in range(N):
                if text1[m] == text2[n] :
                    dp[m+1][n+1] = dp[m][n] + 1
                else:
                    dp[m+1][n+1] = max(dp[m][n+1], dp[m+1][n])
        # print (dp)
        return dp[-1][-1]

s = Solution()
print(s.longestCommonSubsequence("bsbininm", "jmjkbkjkv"))

