from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x : x[1])
        # print(points)
        ans, end = 0 , float('-INF')
        for p in points:
            if p[0] > end:
                ans += 1
                end = p[1]
        return ans

s = Solution()
ip = [[10,16],[2,8],[1,6],[7,12]]
ans = s.findMinArrowShots(ip)
print(ans)