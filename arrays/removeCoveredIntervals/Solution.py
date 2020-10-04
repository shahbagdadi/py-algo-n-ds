from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        prev , ans = [],0
        intervals.sort(key = lambda x : (x[0],-x[1]))
        for itv in intervals :
            if prev and itv[0] >= prev[0] and itv[1] <= prev[1] :
                continue
            ans += 1
            prev = itv
        return ans

s = Solution()
ip = [[1,2],[1,4],[3,4]]
ans = s.removeCoveredIntervals(ip)
print(ans)