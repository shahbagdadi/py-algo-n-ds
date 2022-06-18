from itertools import accumulate



class Solution:
    def minWinSum(self,nums,K) :
        rsum , ans , L = list(accumulate(nums)) , float("inf") , len(nums)
        # print(rsum)
        for s in range(L) :
            for e in range(s,L) :
                if K >=0 and rsum[e] - rsum[s] >= K :
                    ans = min(ans,e-s)
                if K < 0 and rsum[e] - rsum[s] <= K :
                    ans = min(ans,e-s)
        return ans

            

s = Solution()
ip = [-1,4, -1]
ans = s.minWinSum(ip,4)
print(ans)

ip = [-1,2,2,0, -1]
ans = s.minWinSum(ip,4)
print(ans)

ip = [-1,3,-1,2, -1]
ans = s.minWinSum(ip,4)
print(ans)

ip = [-1,3,-1,-2,-1, -1]
ans = s.minWinSum(ip,-4)
print(ans)