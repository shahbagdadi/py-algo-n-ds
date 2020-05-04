from collections import Counter

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ls , lt = len(s) , len(t)
        if ls > lt :
            return self.isOneEditDistance(t,s) 
            
        if lt - ls  > 1 : return False

        for i in range(ls):
            if s[i] != t[i]:
                if ls == lt :
                    return s[i+1:] == t[i+1:] # length same so rest should match
                else:
                    return s[i:] == t[i+1:] # leave this char but rest should match       
        return ls + 1 == lt  # could be true only if all matched in loop but s was a char short

s = Solution()
ans = s.isOneEditDistance('1203', '123')
print(ans)
