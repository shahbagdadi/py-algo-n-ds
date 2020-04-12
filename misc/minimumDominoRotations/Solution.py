
from typing import List
import collections
import sys

class Solution:
    def minDominoRotations1(self, A: List[int], B: List[int]) -> int:
        da = collections.defaultdict(list)
        db = collections.defaultdict(list)
        total , ans = 0 , sys.maxsize
        for i,t in enumerate(zip(A,B),1):
            print(i,t)
            da[t[0]].append(i) 
            db[t[1]].append(i)
            total += i
        print(da)
        print(db)
        for i in range(1,7):
            lst = set(da[i] + db[i])
            print(da[i], db[i])
            if sum(lst) == total :
                ans = min(ans, len(lst) - len(da[i]),  len(lst)- len(db[i]))
        return ans if ans != sys.maxsize else -1

    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        ca , cb , same = collections.Counter(), collections.Counter(), collections.Counter()
        N = len(A)
        for i in range(N):
            ca[A[i]] += 1
            cb[B[i]] += 1
            if A[i] == B[i] :
                same[A[i]] += 1
        for x in range(1,7):
            if ca[x] + cb[x] - same[x] == N:
                return N - max(ca[x], cb[x])
        return -1


s = Solution()
# A = [2,1,2,4,2,2]
# B = [5,2,6,2,3,2]
# A = [3,5,1,2,3]
# B = [3,6,3,3,4]
# A = [1,2,1,1,1,2,2,2]
# B = [2,1,2,2,2,2,2,2]

A = [6,1,6,4,6,6]
B = [5,6,2,6,3,6]
print(s.minDominoRotations(A,B))