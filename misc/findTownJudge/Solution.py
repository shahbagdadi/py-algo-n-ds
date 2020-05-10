from typing import List
import collections

class Solution:
    def findJudge0(self, N: int, trust: List[List[int]]) -> int:
        if not trust : return 1
        pset, jcntr = set(), collections.Counter() 
        for p, t in trust:
            jcntr[t] += 1
            pset.add(p)
        j, _ = jcntr.most_common(1)[0]
        print(j, jcntr, len(pset))
        return j if j not in pset and len(pset) >= N-1 and jcntr[j] == len(pset) else -1

    # Lee215 ->  in-degree - out-degree = N - 1 become the judge
    def findJudge(self, N, trust):
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1

s = Solution()
ip = [[1,3],[2,3],[3,1]]
ans = s.findJudge(4,ip)
print(ans)
        