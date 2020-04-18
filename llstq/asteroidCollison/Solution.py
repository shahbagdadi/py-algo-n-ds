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
        for new in asteroids:
            while stack and new < 0 < stack[-1]:
                if stack[-1] < -new:
                    stack.pop()
                    continue
                elif stack[-1] == -new:
                    stack.pop()
                break
            else:   # exceuted when while loop is false and break not executed. 
                stack.append(new)
                print(stack)
        return stack

s = Solution()
ans = s.asteroidCollision([8,18,-28,5])
print(ans)