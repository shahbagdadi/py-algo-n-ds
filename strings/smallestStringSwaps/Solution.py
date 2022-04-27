from typing import List
from collections import defaultdict
        
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1]*n
        
    def find(self, x):
        if x == self.root[x]: return x
        return self.find(self.root[x])

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N , uf = len(s), UnionFind(len(s))
    
        for parent, child in pairs:
            uf.union(parent, child)
    
        groups = defaultdict(list)
        for i in range(N):
            groups[uf.find(i)].append(s[i]) # append char to its parent root . key=> parent , value => chars

        # Reverse sort we want to pop in the end
        for key in groups.keys():
            groups[key].sort(reverse=True) # sort the values in reverse order
      
# String join is significantly faster then concatenation.
        res = []
        for i in range(N):
            res.append(groups[uf.find(i)].pop())
            
        return "".join(res)


s = Solution()
ip = 'dcab'
pairs = [[0,3],[1,2],[0,2]]
ans = s.smallestStringWithSwaps(ip,pairs)
print(ans)