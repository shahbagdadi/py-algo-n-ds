from typing import List
from collections import defaultdict
from collections import deque

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, squares, q = defaultdict(set), defaultdict(set), defaultdict(set), deque([])
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":          # maintain sets of numbers used
                    rows[r].add(board[r][c])       # row set
                    cols[c].add(board[r][c])        # column set
                    squares[(r // 3, c // 3)].add(board[r][c])  # square set
                else:
                    q.append((r, c))    # add the '.' location to queue
        def dfs():
            if not q:
                return True
            r, c = q[0]
            t = (r // 3, c // 3)
            for n in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                if n not in rows[r] and n not in cols[c] and n not in squares[t]:
                    board[r][c] = n
                    rows[r].add(n)
                    cols[c].add(n)
                    squares[t].add(n)
                    q.popleft()
                    if dfs():
                        return True
                    else:                   #backtrack
                        board[r][c] = "."
                        rows[r].discard(n)
                        cols[c].discard(n)
                        squares[t].discard(n)
                        q.appendleft((r, c))
            return False
        dfs()


s = Solution()
ip = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]
s.solveSudoku(ip)
for r in ip:   
    print(r)
        