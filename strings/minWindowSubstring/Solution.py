from collections import Counter
import sys

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cntr , tcnt , scnt = Counter(t), len(t) , 0
        l , min_left , min_len = 0 , 0 , sys.maxsize
        # keep going right till you find all chars in t
        for r in range(len(s)) :
            cr = s[r]
            if cr in cntr :
                cntr[cr] -= 1
                if cntr[cr] >= 0 : scnt += 1
            while scnt == tcnt :
                # is this min window ?
                if r-l+1 < min_len :
                    min_left, min_len = l , r-l+1
                # shrink the left side 
                cl = s[l]
                if cl in cntr :
                    cntr[cl] += 1
                    if cntr[cl] > 0 : scnt -= 1
                l += 1
        return '' if min_len == sys.maxsize else s[min_left:min_left+min_len]


soln = Solution()
s , t = 'bba' , 'ab'
ans = soln.minWindow(s,t)
print(ans)


