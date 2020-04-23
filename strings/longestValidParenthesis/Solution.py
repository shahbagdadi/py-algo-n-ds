from typing import List
import sys
from collections import deque

class Solution:
    def longestValidParenthesesStack(self, s: str) -> int:
        stack , maxw = [-1] , 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif stack :
                stack.pop()
                if stack:
                    maxw = max(maxw, i - stack[-1])
                else:
                    stack.append(i)
        return maxw

    
    def longestValidParentheses(self, s: str) -> int:
        l, r , maxw = 0,0 , 0
        
        for c in s:
            if c == '(': l += 1
            elif c == ')' : r+=1
            if l == r :
                maxw = max(maxw, l+r)
            if r > l :
                l = r = 0

        l = r = 0
        for c in s[::-1]:
            if c == '(': l += 1
            elif c == ')' : r+=1
            if l == r :
                maxw = max(maxw, l+r)
            if l > r :
                l = r = 0
        return maxw

s = Solution()
ans = s.longestValidParentheses(')()())')
print(ans)