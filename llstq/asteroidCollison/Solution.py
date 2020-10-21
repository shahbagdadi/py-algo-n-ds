from typing import List

class Solution:
    def asteroidCollision1(self, a: List[int]) -> List[int]:
        res , stack = [] , []
        for n in a:
            if n > 0: 
                stack.append(n)
            elif stack:
                while stack:
                    if -n > stack[-1]:
                        stack.pop()
                    elif -n == stack[-1]:
                        stack.pop()
                        n = 0
                        break
                    else:
                        break
            if not stack and n != 0 :
                res.append(n)
        return res + stack

    def asteroidCollision(self, asteroids):
        stack = []
        for num in asteroids:
            if num>0:
                stack.append(num)
            else:
                while stack and stack[-1]>0 and stack[-1]<abs(num):
                    stack.pop()
                if not stack or stack[-1]<0:
                    stack.append(num)
                elif stack[-1] == -num:
                    stack.pop()
        return stack

s = Solution()
ans = s.asteroidCollision([8,18,-28,5])
print(ans)