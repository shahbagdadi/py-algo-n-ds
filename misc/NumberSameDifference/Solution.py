from typing import List

class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        def dfs(N, K, num) :
            if N == 0 : 
                lst.append(num)
                return
            for i in range(10) :
                if i == 0 and num == 0 : # do not add 0 at beginning of num
                    continue
                elif i != 0 and num == 0 :  # no previous num to check with
                    dfs(N-1, K, i)
                else :
                    if abs(num %10 - i ) == K :
                        dfs (N-1, K, num * 10 + i)

        lst = []
        if N == 0 : return []
        if N == 1 : lst.append(0)
        dfs(N, K , 0)
        return lst
                
s = Solution()
ans = s.numsSameConsecDiff(3, 2)
print(ans)

