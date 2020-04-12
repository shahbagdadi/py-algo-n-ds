from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = { 0 : {1,3} , 1 : {0,2,4}, 2: {1, 5}, 3 : {0, 4}, 4: {1,3,5}, 5 :{2,4}} # all possible move from index i after we flatten the board
        seen , depth = set() , 0
        b = ''.join(str(c) for row in board for c in row)
        q = [(b,b.index('0'))]      # start with current borad and the current index of '0' in the board
        while q:
            newq = []        # new queue
            for b,i in q:
                seen.add(b)
                if b == '123450':    # end state so we got our ans
                    return depth
                arr = [ c for c in b]
                for move in moves[i]:       # all possible moves of a '0' from index i
                    new_arr = arr.copy()
                    new_arr[i], new_arr[move] = new_arr[move], new_arr[i]   # swap as part of the move
                    new_b = ''.join(new_arr)
                    if new_b not in seen:       # If I have not seen this new board positions before
                        newq.append((new_b,move))      # new board with new position of '0'
            depth += 1
            q = newq
        return -1

s = Solution()
# ip = [[4,1,2],[5,0,3]]
ip = [[3,2,4],[1,5,0]]
ans = s.slidingPuzzle(ip)
print(ans)