from typing import List

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        N , ans = len(A) , []
        # lg holds the largest in A
        for lg in range(N,1,-1):
            idx = A.index(lg) # find largest and place it in its sorted spot in 2 operations
            ans.append(idx+1)
            ans.append(lg)
            A = A[:idx:-1] + A[:idx] # placed lg in its spot so no longer included
        return ans


s = Solution()
ip = [3,2,4,1]
ans = s.pancakeSort(ip)
print(ans)