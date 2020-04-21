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
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in ('+', '-', '*', '/', ')'):
                update(op, num)
                if c == ')':
                    num = 0
                    print(stack)
                    while isinstance(stack[-1], int):
                        num += stack.pop() 
                    op = stack.pop()
                    update(op, num)
                num, op = 0, c
            elif c == '(':
                stack.append(op)
                num, op = 0, '+'
        update(op, num)
        return sum(stack)

s = Solution()
ans = s.calculate('2 * (15 - 5 + 2) / 3')
print(ans)