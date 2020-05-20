
from typing import List
import bisect

class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        weight = 1
        while self.stk and self.stk[-1][0] <= price :
            weight += self.stk.pop()[1]
        self.stk.append((price,weight))
        return weight

sp = StockSpanner()
print(sp.next(100))
print(sp.next(80))
print(sp.next(60))
print(sp.next(70))
print(sp.next(60))
print(sp.next(75))
print(sp.next(85))
