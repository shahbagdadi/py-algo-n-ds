from typing import List
from collections import defaultdict


class Solution:
    def calculate(self, s: str) -> int:
        def update(op, num):
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop() * num)
            elif op == '/':
                stack.append(int(stack.pop() / num))
        
        stack = []
        num, op = 0, '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in ('+', '-', '*', '/', ')'):
                update(op, num)
                if s[i] == ')':
                    num = 0
                    print(stack)
                    while isinstance(stack[-1], int):
                        num += stack.pop() 
                    op = stack.pop()
                    update(op, num)
                num, op = 0, s[i]
            elif s[i] == '(':
                stack.append(op)
                num, op = 0, '+'
        update(op, num)
        return sum(stack)
        

s = Solution()
ans = s.calculate('(1+(4+5+2)-3)+(6+8)')
print(ans)