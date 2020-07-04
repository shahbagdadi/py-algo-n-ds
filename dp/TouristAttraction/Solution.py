from functools import lru_cache

class Solution:

    def tourist(self,grid):
        N , M = len(grid) , len(grid[0])
        dp = [ [0] * (M+1) for _ in range(N+1)]
        for r in range(1,N+1) :
            for c in range(1,M+1):
                if r % 2 == 0 :
                    dp[r][c] = dp[r-1][c] + grid[r-1][c-1]
                else :
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1]+ grid[r-1][c-1])
            print(dp[r])
        # print(dp)
        return dp[N][M]

s = Solution()
ip = [[0,3,2,4,0],
    [1,0,2,4,3],
    [0,3,2,4,2],
    [4,6,5,2,1],
    [0,0,7,3,4],
    [4,4,5,2,1],
    [0,3,3,0,2],
    [5,6,8,5,3],
    [0,1,3,2,2]
    ]

ans = s.tourist(ip)
print(ans)