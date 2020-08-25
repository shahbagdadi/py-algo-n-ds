from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def feasable(speed):
            return sum(math.ceil(pile / speed) for pile in piles) <= H

        l , r = 1, max(piles)
        while l < r :
            m = (l+r) // 2
            if feasable(m):
                r = m
            else :
                l = m + 1
        return l


s = Solution()
ip = [30,11,23,4,20]
ans = s.minEatingSpeed(ip,5)
print(ans)