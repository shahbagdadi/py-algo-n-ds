from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key =len)    # NlogN
        wdict , cmax = {}, 0
        for w in words:         # N * S * S where S is max length of word
            wmax = 0
            for i in range(len(w)):
                ws = wdict.get(w[:i] + w[i+1:],0) +1
                wmax = max(wmax,ws)
            wdict[w] = wmax  
            cmax = max(cmax,wmax)
        # print(dp)    
        return cmax


s = Solution()
ans = s.longestStrChain(["bca","bda","bdca","a","b","ba",])
print(ans)