from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, tank, start = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if tank < 0 :               # my current stack is no good, maybe next is better
                start = i + 1
                tank = 0
        return start if total >= 0 else -1

s = Solution()
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(s.canCompleteCircuit(gas,cost))