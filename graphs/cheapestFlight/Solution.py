from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        prices , heap = defaultdict(dict) , [(0,src,K+1)]
        for s, d, p in flights:
            prices[s][d] = p 
        while heap:
            price , city , stops = heapq.heappop(heap)
            if city == dst : return price
            if stops > 0 :
                for adj in prices[city] :
                    heapq.heappush(heap,(price + prices[city][adj], adj, stops -1 ))
        return -1

s = Solution()
ip = [[0,1,100],[1,2,100],[0,2,500]]
ans = s.findCheapestPrice(3,ip,0,2,1)
print(ans)