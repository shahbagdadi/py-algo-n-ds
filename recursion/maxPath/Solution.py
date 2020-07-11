from functools import lru_cache

class Solution :

    def maxSumInMatrix(self, grid):

        ans, N , M = 0, len(grid) , len(grid[0])

        @lru_cache(None)
        def helper(r,c,cur_total) :
            nonlocal ans
            if r >= N or c >= M : return 
            cur_total += grid[r][c]
            ans = max(ans, cur_total)
            helper(r,c+1,cur_total)
            helper(r+1,c, cur_total)

        helper(0,0,0)
        return ans

s = Solution()
grid = [[1,2,3],[4,5,6],[7,8,9]]
ans = s.maxSumInMatrix(grid)
print(ans)