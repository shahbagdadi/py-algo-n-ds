import sys
from collections import deque

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = sys.maxsize
        self.stk = deque()

    def push(self, x: int) -> None:
        if x <= self.min:
            self.stk.append(self.min)
            self.min = x
        self.stk.append(x)

    def pop(self) -> None:
        x = self.stk.pop()
        if x == self.min :
            self.min = self.stk.pop()
        return x


    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min
        

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
print(obj.pop())
print(obj.getMin())
print(obj.top())