from typing import List
import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_ints = sorted([[s,e,i] for i,[s,e] in enumerate(intervals)])
        begs = [s for s,_,_ in sorted_ints]
        out = [-1]*len(begs)
        for s,e,i in sorted_ints:
            t = bisect.bisect_left(begs, e)
            if t < len(begs):
                out[i] = sorted_ints[t][2]   
        return out

s = Solution()
ip = [[1,12],[2,9],[3,10],[13,14],[15,16],[16,17]]
ans = s.findRightInterval(ip)
print(ans)