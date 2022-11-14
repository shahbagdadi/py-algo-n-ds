from itertools import accumulate
from collections import deque



class Solution:

    # Brute Force    T - O(n^2)    S - O(1)  
    def minWinSumBF(self,nums,K) :
        ans , L = float("inf"), len(nums)
        if K <=0 :
            return 1  if any( n >= K for n in nums) else ans
        for s in range(L) :
            csum = nums[s]
            if csum >= K : return 1
            for e in range(s+1,L) :
                if csum >= K :
                    ans = min(ans,e-s)
                    break
                csum += nums[e]
        return ans


    # T - O(n)    S - O(n)
    def minWinSum(self,nums,K) :
        ans , L = float("inf"), len(nums)
        if K <=0 :
            return 1  if any( n >= K for n in nums) else ans
        csum , q = 0, deque([(-1,0)]) # monotonic increasing deque storing possible start indexes (index,csum)
        for i, n in enumerate(nums):
            csum += n
            if n > 0:
                while q and csum - q[0][1] >= K:
                    ans = min(ans, i-q.popleft()[0]) # shrink win on left
            else:
                while q and csum <= q[-1][1]:       # if csum less that the last sum in queue
                    q.pop()                         # shrink win on right
            q.append((i, csum))
        return ans 

            

s = Solution()
ip = [-1,2,2, -1]
print(s.minWinSumBF(ip,4)) # 2 -> {2,2}

ip = [-1,2,2,0, -1]
print(s.minWinSumBF(ip,4)) # 2 -> {2,2}

ip = [-1,3,-1,2, -1]
print(s.minWinSumBF(ip,4)) # 3 -> {3,-1,2}

ip = [-1,3,-1,-2,-1, -1]
print(s.minWinSumBF(ip,-4)) # 1 -> {-1}

# Optimized 
ip = [-1,2,2, -1]
print(s.minWinSum(ip,4)) # 2 -> {2,2}

ip = [-1,2,2,0, -1]
print(s.minWinSum(ip,4)) # 2 -> {2,2}

ip = [-1,3,-1,2, -1]
print(s.minWinSum(ip,4)) # 3 -> {3,-1,2}

ip = [-1,3,-1,-2,-1, -1]
print(s.minWinSum(ip,-4)) # 1 -> {-1}