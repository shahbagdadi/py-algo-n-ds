
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ## store parent of each node 
        p = [x for x in range(len(edges)+1)]
        
        def find(x):
            # if x has a parent, trave to its parent 
            if p[x] != x: p[x] = find(p[x])
            return p[x]
        
        def union(x, y):
            # if x and Y have a common parent return true
            if find(x) == find(y): return True
            # make y the parent of the parent of x
            p[find(x)] = find(y)
        
        for x, y in edges:
            # keep finding the common parent and if they have one then [x,y] is breaking link
            if union(x,y): return [x, y]


s = Solution()
ip = [[1,2],[2,3],[3,4],[1,4],[1,5]]
ans = s.findRedundantConnection(ip)
print(ans)