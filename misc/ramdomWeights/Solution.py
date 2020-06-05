
from typing import List
import random
import bisect
class Solution:

    def __init__(self, w: List[int]):
        self.weights , self.idx = [0], 0
        for i in range(len(w)):
            self.weights.append(self.weights[-1] + w[i])

    def pickIndex(self) -> int:
        rand = random.randint(1, self.weights[-1])
        idx = bisect.bisect_left(self.weights, rand)
        return idx - 1


# Your Solution object will be instantiated and called as such:
w = [1,3]
obj = Solution(w)
print(obj.pickIndex())
print(obj.pickIndex())