from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        cmax , cmin , ans = -10000 , 10000 , 0
        for arr in arrays :
            ans = max (ans, arr[-1] - cmin, cmax - arr[0])
            cmax , cmin = max(cmax, arr[-1]) , min(cmin,arr[0])
        return ans


s = Solution()
# ip = [[1,2,3],[4,5],[1,2,3]]
ip = [[1,5],[3,4]]
ans = s.maxDistance(ip)
print(ans)