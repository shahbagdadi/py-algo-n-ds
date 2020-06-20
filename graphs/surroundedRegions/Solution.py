from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        
        R, C , queue = len(board), len(board[0]), deque([])
        for r in range(R):
            for c in range(C):
                if (r in [0, R-1] or c in [0, C-1]) and board[r][c] == "O":
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            if 0 <= r < R and 0 <= c < C and board[r][c] == "O":
                board[r][c] = "D"
                queue.extend([ (r - 1, c), (r+1, c), (r, c-1), (r, c+1) ])
            
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "D":
                    board[r][c] = "O"
        
s = Solution()
ip = [  ['X', 'X', 'X', 'X'], 
        ['X', 'O', 'O', 'X'], 
        ['X', 'X', 'O', 'X'], 
        ['X', 'O', 'X', 'X'] ]
s.solve(ip)
for r in range(len(ip)):
    print(ip[r])