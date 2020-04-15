from typing import List
import collections
import sys

class Solution:
    def findMinDifference1(self, timePoints: List[str]) -> int:
        times , res = [] , sys.maxsize
        for t in timePoints:
            h, m = t.split(':')
            times.append(int(h) *  60 + int(m))
        times.sort()
        print(times)
        for i, m in enumerate(times):
            if i == 0 :
                res = min(res,m + (24 * 60 - times[-1]))
            res = min(res, abs(m - times[i-1]))
        return res

    def findMinDifference(self, timePoints: List[str]) -> int:
        times = sorted(int(t[:2]) * 60 + int(t[-2:]) for t in timePoints)
        times.sort()
        times.append(times[0] + 24*60)
        return min( t2 - t1 for t1, t2 in zip(times , times[1:]))



s = Solution()
ans = s.findMinDifference(["23:59","00:00"])
print(ans)
