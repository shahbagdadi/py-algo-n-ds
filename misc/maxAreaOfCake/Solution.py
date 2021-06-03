from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hc , vc = sorted(horizontalCuts) +[h], sorted(verticalCuts) + [w]
        mh , p = 0 , 0
        for h in hc :
            mh = max(mh,h-p)
            p = h
        mw , p = 0 , 0
        for w in vc :
            mw = max(mw,w-p)
            p = w
        return mh * mw

s = Solution()
hc = [1,2,4]
vc = [1,3]
# hc = [3,1]
# vc = [1]
ans = s.maxArea(5,4,hc,vc)
print(ans)