from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cntd = {0:0}
        cnt ,maxlen = 0 , 0
        for i,n in enumerate(nums,1):
            cnt = cnt + 1 if n == 1 else cnt -1
            if cnt in cntd:
                maxlen = max(maxlen, i - cntd[cnt])
            else:
                cntd[cnt] = i
        return maxlen

s = Solution()
ans = s.findMaxLength([0,1,0,0,0,1,0,1,1])
print(ans)
            



        



