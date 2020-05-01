from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        def neighbors(x,y):
            steps = ( (0,1), (1,1) , (1,0), (1, -1), (0, -1), (-1, -1), (-1,0) , (-1,1))
            for step in steps:
                nx , ny = x + step[0] , y + step[1] 
                if 0 <= nx < N and 0 <= ny < M:
                    yield (nx,ny)

        def reveal(p,q):
            if board[p][q] != 'E': return
            cnt = 0
            for nei in neighbors(p,q):
                x, y = nei
                if board[x][y] == 'M':
                    cnt +=1
            if cnt == 0 :
                board[p][q] = 'B'
            else:
                board[p][q] = str(cnt)
                return
            for nei in neighbors(p,q):
                reveal(nei[0], nei[1])

        x , y = click
        N , M = len(board), len(board[0])
        if board[x][y] == 'M' :
            board[x][y] = 'X'
        else:
            reveal(x,y)  
        return board


s= Solution()
board = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

click = [3,0]
b = s.updateBoard(board,click)
print(b)