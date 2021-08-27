from collections import deque

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        po , s = preorder.split(','), []
        for n in po :
            while s and s[-1] == n == '#' :
                s.pop()
                if not s : return False
                s.pop()
            s.append(n)
        return s == ['#']

s = Solution()
ip = "9,3,4,#,#,1,#,#,2,#,6,#,#"
ans = s.isValidSerialization(ip)
print(ans)