
from typing import List
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        N , M = len(s1) , len(s2)
        pCtr = Counter(s1)
        print(pCtr)
        window = Counter(s2[:N])
        for i in range(N,M):
            print(window)
            if +window == pCtr :
                return True            
            minus = Counter(s2[i - N])
            add = Counter(s2[i])
            window -= minus
            window += add
        return window == pCtr

s = Solution()
ans = s.checkInclusion('ab', 'eidbaooo')
print(ans)