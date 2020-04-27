from functools import lru_cache

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        @lru_cache(None)
        def helper(x,y):
            if x == y and x == 0: # you can also do x + y == 0
                return 0
            if x + y == 2 :        # you need 2 moves from 1,1 or 0,2
                return 2
            return min(helper(abs(x-1),abs(y-2)), helper(abs(x-2),abs(y-1))) +1 # min distance to next step + 1 

        return helper(abs(x), abs(y))   # does not matter if x,y is +ve or -ve the dist is still the same

s = Solution()
ans = s.minKnightMoves(5,5)
print(ans)