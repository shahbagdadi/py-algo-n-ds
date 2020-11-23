from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mset = set()
        for word in words :
            mw = ''
            for c in word :
                mw += morse[ord(c) - ord('a')]
            mset.add(mw)
            # print(mw)
        return len(mset)

s = Solution()
ip = ["gin", "zen", "gig", "msg"]
ans = s.uniqueMorseRepresentations(ip)
print(ans)