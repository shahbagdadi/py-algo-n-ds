from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C, res , q , visited = len(image), len(image[0]) , image.copy() , deque([(sr,sc)]) , set()
        startColor = image[sr][sc]
        
        def neighbors(node):
            steps = ((0,1), (1,0) , (0, -1), (-1,0))
            for s in steps:
                nr,nc = node[0] + s[0] , node[1] + s[1]
                if 0 <= nr < R and 0 <= nc < C and image[nr][nc] == startColor:
                    yield (nr, nc)

        while q:
            node = q.pop()
            # print(node)
            res[node[0]][node[1]] = newColor
            for n in neighbors(node):
                if n not in visited:
                    visited.add(n)
                    q.appendleft(n)
        return res
        


        

s = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
ans = s.floodFill(image,1,1,2)
print(ans)