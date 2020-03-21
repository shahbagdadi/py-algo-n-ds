from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # deadend marked already as visited
        cnt, v, q = 0, set(deadends), deque(['0000'])
        if "0000" in v: return -1
        q.append(None)  # marker
        while len(q):
            n = q.popleft()
            if n == None:  # if marker hit that means all sibling nodes exhausted
                cnt += 1    # increment count
                if q and q[-1]:  # queue not empty and has valid nodes
                    q.append(None)  # mark current nodes in queue as sibling
            elif n == target:
                return cnt
            else:
                for i, c in enumerate(n):
                    num = int(c)
                    sf = n[:i] + str(num+1) + n[i +
                                                1:] if num < 9 else n[:i] + str(0) + n[i+1:]
                    sb = n[:i] + str(num-1) + n[i +
                                                1:] if num > 0 else n[:i] + str(9) + n[i+1:]
                    if sf not in v:
                        v.add(sf)
                        q.append(sf)
                    if sb not in v:
                        v.add(sb)
                        q.append(sb)
        return -1


s = Solution()
a = s.openLock(["0201", "0101", "0102", "1212", "2002"], "0202")
print(a)
