from typing import List
from itertools import accumulate
import bisect
import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        Area = [(x2-x1+1)*(y2-y1+1) for x1,y1,x2,y2 in rects]
        self.weights = [a/sum(Area) for a in accumulate(Area)]
        self.rects = rects 

    def pick(self) -> List[int]:
        # pick a random weight and find it in the weight array. Larger rect will have higher probability
        idx_rect = bisect.bisect(self.weights, random.random())
        x1, y1, x2, y2 = self.rects[idx_rect] 
        # find a random point in this rectangle
        return [random.randint(x1, x2),random.randint(y1, y2)]
        


# Your Solution object will be instantiated and called as such:
ip = [[-2,-2,-1,-1],[1,0,3,0]]
s = Solution(ip)
for i in range(5):
    print(s.pick())