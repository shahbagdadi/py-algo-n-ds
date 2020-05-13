
from typing import List
from functools import lru_cache

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        for d in num:
            while k > 0 and stk and stk[-1] > d:
                stk.pop()
                k -= 1
            stk.append(d)
        print(stk)
        if k > 0:
            stk = stk[:-k]
        return ''.join(stk).lstrip('0') or '0'

s = Solution()
ip = '10200'
k = 1
ans = s.removeKdigits(ip,k)
print(ans)