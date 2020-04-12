
from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while stones:
            if len(stones) == 1:
                return -1 * heapq.heappop(stones)
            else:
                s1 = heapq.heappop(stones)
                s2 = heapq.heappop(stones)
                if s1 != s2 : 
                    heapq.heappush(stones,s1 - s2)
        return 0



s = Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))