from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dtix = defaultdict(list)
        for tix in sorted(tickets)[::-1]:
            dtix[tix[0]].append(tix[1])
        # print(dtix)
        route , stack  = [] , ['JFK']
        while stack:
            while dtix[stack[-1]]:
                dest = dtix[stack[-1]].pop()
                # print(f'pushing to stack {dest}')
                stack.append(dest) 
            # print(f'poping from {stack}')
            route.append(stack.pop())
        return route[::-1]

s = Solution()
ip = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
ans = s.findItinerary(ip)
print(ans)