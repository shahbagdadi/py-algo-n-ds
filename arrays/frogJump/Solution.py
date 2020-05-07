from typing import List
from collections import defaultdict

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        d = {x: set() for x in stones}
        d[1].add(1) # since first stone is always 0 and jump to stone[1] is 1
        for x in stones[:-1]:
            for j in d[x]:
                for k in range(j-1, j+2):
                    if k > 0 and x+k in d:
                        d[x+k].add(k)
        return bool(d[stones[-1]])
        

s = Solution()
ip = [0,1,3,5,6,8,12,17]
# ip = [0,1,2,3,4,8,9,11]
ans = s.canCross(ip)
print(ans)
