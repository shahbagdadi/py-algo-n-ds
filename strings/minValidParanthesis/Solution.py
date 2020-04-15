from typing import List
import collections

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def removeBracket(s,b1,b2):
            sb , cnt = [] , 0
            for c in s:
                if c == b1 :
                    cnt += 1
                elif c == b2 :
                    if cnt == 0 :
                        continue
                    else:
                        cnt -= 1
                sb.append(c)
            return ''.join(sb)
        
        ans = removeBracket(s,'(' , ')')
        # print(ans)
        ans = removeBracket(ans[::-1], ')' , '(')
        return ans[::-1]

s = Solution()
ans = s.minRemoveToMakeValid('a)b(c)d')
print(ans)
