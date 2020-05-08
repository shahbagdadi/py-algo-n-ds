from typing import List
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0 : return 0
        ctr , res = Counter(nums) , 0
        for n in ctr :
            if (k > 0 and n + k in ctr) or (k == 0 and ctr[n] > 1) :
                res += 1
        return res

s = Solution()
ip = [1,3,1,5,1,4]
ans = s.findPairs(ip,0) 
print(ans)