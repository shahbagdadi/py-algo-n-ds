from typing import List
import itertools

class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        c , ans = 0, []
        for n1,n2 in itertools.zip_longest(num1[::-1], num2[::-1], fillvalue=0):
            c += int(n1) + int(n2)
            ans.append(str(c%10))
            c = c // 10
        if c : ans.append(str(c))
        return ''.join(ans[::-1])

            
s = Solution()
ans = s.addStrings('99', '101')
print(ans)