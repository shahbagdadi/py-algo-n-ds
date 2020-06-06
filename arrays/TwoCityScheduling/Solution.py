from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key =lambda x : x[0] - x[1])
        n , total = len(costs)//2 , 0
        for i in range(n):
            total += costs[i][0] + costs[i+n][1]
        return total

        
s = Solution()
ip = [[10,20],[30,200],[400,50],[30,20]]
ans = s.twoCitySchedCost(ip)
print(ans)