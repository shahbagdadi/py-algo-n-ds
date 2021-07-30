from typing import List
from collections import deque
import sys

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R, C, q = len(mat), len(mat[0]), deque()
        for r in range(R) :
            for c in range(C) :
                if mat[r][c] == 0 : 
                    q.appendleft((r,c))
                else :
                    mat[r][c] = sys.maxsize

        while q :
            r,c = q.pop()
            steps = ((r-1,c) , (r,c+1) , (r+1, c), (r, c-1))
            for nr,nc in steps :
                if 0 <= nr < R and 0 <= nc < C and mat[nr][nc] > mat[r][c]: 
                    mat[nr][nc] = mat[r][c] + 1
                    q.appendleft((nr,nc))
        return mat
            
s = Solution()
ip = [[0,0,0],[0,1,0],[1,1,1]]
ans = s.updateMatrix(ip)
print(ans)