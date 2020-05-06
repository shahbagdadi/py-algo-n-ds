from typing import List
from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split('/')
        stk = []
        for token in tokens:
            if token == '..' :
                if stk : stk.pop()
            elif token and token != '.':
                stk.append(token)
        return '/' + '/'.join(stk)


s = Solution()
ip = '/a//b////c/d//././/..'
# ip = '/../'
ans = s.simplifyPath(ip)
print(ans)

