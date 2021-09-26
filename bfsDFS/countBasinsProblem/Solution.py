from typing import DefaultDict
from functools import lru_cache

class Solution:
    def countBasin(self, mat) :
        m , n , scnt , visited = len(mat) , len(mat[0]) , DefaultDict(int), set()
        
        @lru_cache
        def get_sink(r,c):
            sr , sc = r , c
            for r1,c1 in [(r,c-1),(r,c+1),(r-1,c),(r+1,c)] : # find my lowest neighbor
                if 0<=r1<m and 0<=c1<n and mat[r1][c1] < mat[sr][sc] :
                    sr , sc = r1, c1
            if sr == r and sc == c : # if no other lower neighbor than this is a sink
                sink = (sr,sc)
            else :
                sink = get_sink(sr,sc) # find the sink for my lowest neighbor
            scnt[sink] += 1
            return sink
            
        for r in range(m) :
            for c in range(n) :
                if (r,c) not in visited : get_sink(r,c)
        return sorted([ v for k,v in scnt.items()])
        

s = Solution()
# ip = [[1, 5, 2],[2, 4, 7],[3, 6, 9]]
ip = [[0, 2, 1, 3],[2, 1, 0, 4],[3, 3, 3, 3],[5, 5, 2, 1]]
ans = s.countBasin(ip)
print(ans)