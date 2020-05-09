from typing import List
import collections

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.w = width
        self.h = height
        self.score = 0
        self.path = collections.deque([[0,0]])
        self.foodloc = collections.deque(food)
        self.dir = { 'U' : (-1,0) , 'D' : (1, 0) , 'L' : (0,-1) ,  'R' : (0,1) }
        if self.foodloc:
            self.foodnow = self.foodloc.popleft()
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        curr = self.path[-1]
        dx , dy = self.dir[direction]
        new = [curr[0] + dx , curr[1] + dy]

        #snake crosses the screen boundary 
        if new[0]<0 or new[0]>=self.h or new[1]<0 or new[1]>=self.w:
            return -1

        # snake bites its body
        if new in self.path and new != self.path[0]:
            return -1
            
        if new == self.foodnow:
            self.score += 1
            self.path.append(new)
            if self.foodloc:
                self.foodnow = self.foodloc.popleft()
            else:
                self.foodnow = []
                # There's no more food
        else:
            self.path.append(new)
            self.path.popleft()
            
        return self.score



        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
food = [[1,2],[0,1]]
g = SnakeGame(3,2,food)
print(g.move('R'))
print(g.move('D'))
print(g.move('R'))
print(g.move('U'))
print(g.move('L'))
print(g.move('U'))